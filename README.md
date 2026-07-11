# AI 知识库助手 — Week 1 学习记录

> 📅 2026.07.10 ~ 2026.07.11  
> 👤 feiyuai  
> 🎯 目标：6 周从零到 RAG 知识库系统上线

---

## Day 1：环境搭建 + Hello World

- ✅ Python 3.13 已安装
- ✅ VS Code 开发环境
- ✅ Git 2.53 配置完成
- ✅ 第一个程序：`print("Hello World")`

**核心概念：**
- Python 是解释型语言，写完就能跑
- `print()` 把内容输出到屏幕
- `#` 开头的是注释，Python 不执行

---

## Day 2：Python 生存级语法

### 变量与数据类型
```python
name = "飞宇"        # str  字符串
age = 22             # int  整数
score = 95.5         # float 浮点数
is_pass = True       # bool 布尔值
```

### 条件判断（if/elif/else）
```python
if age >= 18:
    print("已成年")
else:
    print("未成年")
```
⚠️ Python 没有花括号 `{}`，用**缩进**表示代码块。冒号不能忘！

### 循环（for/while）
```python
for i in range(5):          # 0,1,2,3,4
    print(i)

while count <= 5:           # 条件成立就一直跑
    count += 1
```

### 函数（def）
```python
def add(a, b):
    """返回两个数的和"""
    return a + b
```
- `def` 定义函数，不写参数类型和返回类型
- Python 靠缩进判断函数体范围

### 关键对比：Python vs C++

| 概念 | C++ | Python |
|------|-----|--------|
| 变量 | `int x = 5;` | `x = 5` |
| 代码块 | `{ }` | 缩进（4空格） |
| if | `if (x > 0) { }` | `if x > 0:` |
| for | `for (int i=0; i<n; i++)` | `for i in range(n):` |
| 函数 | `int add(int a) { }` | `def add(a):` |
| 空值 | `nullptr` | `None` |

### ⚠️ 踩坑记录

| 坑 | 原因 | 教训 |
|----|------|------|
| `=` vs `<` | `age = 10` 是赋值，`age < 15` 是比较 | 一个等号赋值，比较用 `<` `>` `==` |
| `age < 15` 写在 if 里 | 算出了 True/False 但没存也没输出 | 比较结果必须赋值或 print |

---

## Day 3：数据结构 + 文件读写

### 列表 list
```python
fruits = ["苹果", "香蕉", "橘子"]
fruits[0]       # "苹果" — 下标从0开始
fruits[-1]      # "橘子" — 负数倒着数
fruits[1:3]     # ["香蕉", "橘子"] — 切片
fruits.append("西瓜")   # 追加
len(fruits)     # 长度
```

### 字典 dict
```python
student = {"name": "飞宇", "age": 22, "score": 95}
student["name"]           # "飞宇"
student["weight"] = 70    # 添加新键值对
student.get("address", 0) # 安全取值，没有就返回默认值
```

### 文件读写
```python
# 读
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 读全部
    words = content.split()   # 按空格切词

# 写
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

### 综合练习：单词统计程序 ✅

实现了 `word_count.py`：读取文件 → 切词 → 字典统计词频

```python
counts[word] = counts.get(word, 0) + 1  # 核心一行
```

---

## Day 4：Git 版本控制

### 核心概念
- **仓库**：被 Git 管理的文件夹
- **commit**：一次存档
- **GitHub**：代码托管平台（远程仓库）

### 日常四步循环
```bash
git status                 # 看状态
git add 文件名              # 加入暂存区
git commit -m "说明"       # 本地存档
git push                   # 推送到 GitHub
```

### 配置信息
```bash
git config --global user.name "feiyuai"
git config --global user.email "3553264347@qq.com"
```

### .gitignore — 防止敏感文件泄露
```
.env
__pycache__/
*.pyc
data/
venv/
```

---

## Day 5：AI 辅助编程

### 核心理念
> AI 是副驾驶，我是机长。AI 省打字时间，不省思考时间。

### Prompt 四要素
| 要素 | 说明 | 例子 |
|------|------|------|
| 技术栈 | 用什么语言/框架 | "用 Python" |
| 输入 | 函数收到什么 | "接收命令行参数" |
| 输出 | 函数返回什么 | "输出到终端" |
| 约束 | 特殊要求 | "只用标准库" |

### 综合练习：待办事项程序 ✅

用 Claude Code 生成 `todo.py`，实现了：
- `python todo.py add "内容"` — 添加
- `python todo.py list` — 列出
- `python todo.py done 编号` — 标记完成
- `python todo.py delete 编号` — 删除
- 数据持久化到 `todo.json`

**学到的新知识：**
- `json.load()` / `json.dump()` — JSON ↔ Python 对象互转
- `sys.argv` — 命令行参数（≈ C++ 的 argc/argv）
- `os.path.exists()` — 检查文件是否存在
- `datetime.now().strftime()` — 格式化时间
- `if __name__ == "__main__"` — Python 入口模式

---

## 📁 项目文件结构

```
e:\ai-knowledge-assistant\
├── .gitignore          # Git 忽略规则
├── todo.py             # 待办事项 CLI 程序
├── todo.json           # 待办事项数据文件
├── work.py             # 字符串练习
└── README.md           # 本文件
```

---

## 🎯 Week 1 总结

| 维度 | 掌握程度 |
|------|---------|
| Python 基础语法 | 能看懂、能改代码 |
| 数据结构（list/dict） | 会基本操作、会遍历 |
| 文件读写 + JSON | 能读写文件、能持久化数据 |
| Git 版本控制 | 会 add/commit/push |
| AI 辅助编程 | 会给 Prompt、会调试 AI 代码 |

---

## 📅 下周计划（Week 2）

- FastAPI 项目骨架
- GET/POST/PUT/DELETE 接口
- MySQL 安装 + SQLAlchemy ORM
- 文件上传接口（PDF/TXT 解析）
- 推送到 GitHub

---

> 🚀 6 周的目标：一个能写进简历的 RAG 知识库问答系统
