#!/usr/bin/env python3
"""代办事项管理程序 - 数据存储在 todo.json"""

import json
import os
import sys
from datetime import datetime

# 修复 Windows 下 GBK 编码无法输出 emoji 的问题
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

DATA_FILE = "todo.json"


def load_todos():
    """从文件加载待办列表"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def save_todos(todos):
    """保存待办列表到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def cmd_add(description):
    """添加待办事项"""
    todos = load_todos()
    todo = {
        "id": max([t.get("id", 0) for t in todos], default=0) + 1,
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ 已添加待办 #{todo['id']}: {description}")


def cmd_list():
    """列出所有待办事项"""
    todos = load_todos()
    if not todos:
        print("📭 暂无待办事项")
        return
    print("=" * 50)
    print(f"{'编号':<6}{'状态':<8}待办内容")
    print("-" * 50)
    for t in todos:
        status = "✅ 已完成" if t.get("done") else "⏳ 未完成"
        desc = t.get("description", "")
        print(f"#{t.get('id', '?'):<5}{status:<8}{desc}")
    print("=" * 50)


def cmd_done(todo_id):
    """标记待办事项为已完成"""
    todos = load_todos()
    for t in todos:
        if t.get("id") == todo_id:
            if t.get("done"):
                print(f"⚠️  待办 #{todo_id} 已经是完成状态")
            else:
                t["done"] = True
                t["done_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_todos(todos)
                print(f"🎉 待办 #{todo_id} 已完成: {t.get('description')}")
            return
    print(f"❌ 找不到编号为 #{todo_id} 的待办")


def cmd_delete(todo_id):
    """删除待办事项"""
    todos = load_todos()
    for i, t in enumerate(todos):
        if t.get("id") == todo_id:
            desc = t.get("description", "")
            todos.pop(i)
            save_todos(todos)
            print(f"🗑️  已删除待办 #{todo_id}: {desc}")
            return
    print(f"❌ 找不到编号为 #{todo_id} 的待办")


def print_usage():
    """打印使用帮助"""
    print("代办事项管理程序")
    print()
    print("用法:")
    print("  python todo.py add    <内容>    添加待办")
    print("  python todo.py list             列出所有待办")
    print("  python todo.py done   <编号>    标记完成")
    print("  python todo.py delete <编号>    删除待办")
    print()
    print("示例:")
    print('  python todo.py add "学Python"')
    print("  python todo.py done 1")
    print("  python todo.py delete 1")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("❌ 请输入待办内容")
            print('示例: python todo.py add "学Python"')
            sys.exit(1)
        cmd_add(sys.argv[2])

    elif command == "list":
        cmd_list()

    elif command == "done":
        if len(sys.argv) < 3:
            print("❌ 请输入待办编号")
            print("示例: python todo.py done 1")
            sys.exit(1)
        try:
            todo_id = int(sys.argv[2])
        except ValueError:
            print("❌ 编号必须是整数")
            sys.exit(1)
        cmd_done(todo_id)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("❌ 请输入待办编号")
            print("示例: python todo.py delete 1")
            sys.exit(1)
        try:
            todo_id = int(sys.argv[2])
        except ValueError:
            print("❌ 编号必须是整数")
            sys.exit(1)
        cmd_delete(todo_id)

    else:
        print(f"❌ 未知命令: {command}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
