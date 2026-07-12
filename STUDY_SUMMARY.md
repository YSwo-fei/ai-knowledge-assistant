# 学习总结

## 作用

这个文档是当前阶段的复习提纲，帮助我快速回顾已经掌握的知识点。

## Python 基础

- 赋值用 `=`
- 比较用 `==`、`<`、`>`、`<=`、`>=`
- 字符串必须加引号
- Python 用缩进代替大括号

示例：

```python
name = "feiyuai"
age = 18

if age >= 18:
    print("成年")
```

## 常用数据结构

### 列表

```python
items = ["a", "b", "c"]
items[0]
len(items)
```

### 字典

```python
data = {"name": "feiyuai"}
data["name"]
data.get("age", 0)
```

## 文件操作

读取文件：

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

写入文件：

```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

## Git 复习

- `git add`：加入暂存区
- `git commit`：生成本地提交
- `git push`：推送到 GitHub

## FastAPI 复习

### GET

用于向服务器获取数据。

### POST

用于向服务器提交数据。

### Pydantic

`BaseModel` 用来定义请求数据格式。

```python
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    context: str
```

## `422` 错误含义

`422 Unprocessable Content` 表示：

- 请求已经到达后端
- 但是请求体数据不符合模型要求

常见原因：

- 缺少字段
- 字段名错误
- 字段类型错误

## 当前实践文件

- `todo.py`
- `work.py`
- `main.py`
- `schemy.py`
- `model.py`
- `datebase.py`

## 当前学习重点

当前最重要的三件事：

1. 理解 FastAPI 如何接收和校验请求
2. 理解请求模型和数据库模型的区别
3. 把文档 CRUD 一步一步做出来
