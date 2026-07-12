# AI 知识库助手学习记录

这个仓库用于记录我从 Python 基础开始，逐步走向 AI 知识库助手项目的学习过程。

## 当前进度

目前已经完成从 Python 入门到 FastAPI 初步上手的过渡，开始进入后端接口和数据库模型的学习阶段。

已经完成的内容：

- Python 基础语法：变量、条件判断、循环、函数
- 常用数据结构：列表、字典
- 文件读写
- Git 基本使用
- AI 辅助编程实践
- 命令行待办事项程序
- FastAPI 初步体验
- Pydantic 请求模型
- `422 Unprocessable Content` 错误排查

## 当前仓库文件说明

- `todo.py`：命令行待办事项程序
- `todo.json`：待办事项数据文件
- `work.py`：单词统计练习程序
- `main.py`：当前 FastAPI 练习入口文件
- `schemy.py`：当前 Pydantic 数据模型练习文件
- `model.py`：当前 SQLAlchemy 模型练习文件
- `datebase.py`：当前数据库连接练习文件

说明：

- 这些文件名目前保留了学习阶段的真实状态
- 其中部分文件名还不规范，例如 `datebase.py`、`schemy.py`、`requirement.txt`
- 后续会统一重构为更正式的项目结构

## 我目前学到的核心内容

### 1. Python 基础语法

重点理解：

- 变量是存数据的“盒子”
- 字符串要加引号
- `if / else` 控制分支
- `for / while` 控制重复
- `def` 用来定义函数
- Python 用缩进表示代码块

示例：

```python
age = 16

if age >= 18:
    print("成年")
else:
    print("未成年")
```

### 2. 列表和字典

列表用于存放一组有顺序的数据：

```python
fruits = ["苹果", "香蕉", "橘子"]
print(fruits[0])
print(len(fruits))
```

字典用于存放键值对：

```python
student = {"name": "feiyuai", "age": 22}
print(student["name"])
```

### 3. 文件读写

读取文件：

```python
with open("a.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

写入文件：

```python
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

### 4. 单词统计练习

`work.py` 的作用是读取一个文件，按空白切分内容，再统计每个词出现的次数。

核心代码：

```python
count[word] = count.get(word, 0) + 1
```

它的意思是：

- 如果这个词已经出现过，就在原有次数上加 1
- 如果这个词还没出现过，就从 0 开始计数

### 5. Git 基础

最常用的工作流：

```bash
git status
git add .
git commit -m "说明"
git push
```

重点区分：

- `git add`：加入暂存区
- `git commit`：生成一次本地提交
- `git push`：把本地提交推送到 GitHub

### 6. AI 辅助编程

我已经开始用 AI 帮助生成代码，但重点不是“复制代码”，而是：

- 理解函数在做什么
- 理解数据流向
- 理解命令行参数如何传入
- 看懂报错并修复

### 7. FastAPI 初步体验

基础示例：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}
```

FastAPI 的特点：

- 自动解析请求
- 自动校验类型
- 自动生成 `/docs` 文档页面

### 8. Pydantic 请求模型

示例：

```python
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    context: str
    file_size: int = 0
    file_type: str = "text"
```

这个模型的作用是规定前端发送的数据格式。

需要理解：

- 没有默认值的字段是必填字段
- 有默认值的字段是可选字段
- FastAPI 会把 JSON 自动转换成 Python 对象

这就是为什么代码里可以直接写：

```python
document.title
```

因为 `document` 已经不是普通字典，而是 Pydantic 帮我们创建好的对象。

### 9. `422 Unprocessable Content` 的含义

这个错误表示：

- 请求已经到达服务器
- 但是请求体中的 JSON 数据不符合后端要求

常见原因：

- 缺少必填字段
- 字段名写错
- 字段类型不对

例如后端要求：

```json
{
  "title": "测试",
  "context": "正文"
}
```

但前端发送了：

```json
{
  "title": "测试",
  "content": "正文"
}
```

这时就会返回 `422`。

### 10. GET 和 POST 的区别

最简单的记忆方式：

- `GET`：向服务器要数据
- `POST`：向服务器交数据

例子：

- 打开 `/api/info` 通常是 `GET`
- 创建文档通常是 `POST`

## 当前代码状态

目前项目还处在学习和过渡阶段，还没有完全重构。

当前已知问题：

- 文件命名不规范：
  - `datebase.py` 后续应该改为 `database.py`
  - `schemy.py` 后续应该改为 `schemas.py`
  - `model.py` 后续应该改为 `models.py`
  - `requirement.txt` 后续应该改为 `requirements.txt`
- 早期编辑时存在中文编码混乱，后续需要统一为 UTF-8
- `main.py` 目前还是练习版，不是最终的正式项目结构
- 文档数据还没有完整写入数据库

这些都属于当前学习阶段的正常现象。当前最重要的是先理解概念，再逐步标准化代码结构。

## 已经解决过的典型问题

学习过程中真实踩过的坑：

- `BaseModelc` 写成了错误名字
  - 说明导入名必须完全正确
- `eho=False` 写错成了错误参数
  - 说明关键字参数必须严格拼写正确
- `content` 和 `context` 不一致
  - 说明请求模型字段必须和实际发送的数据保持一致
- `git add` 和 `git commit` 的概念混淆
  - 说明暂存和提交是两个不同步骤
- 编辑器里改了代码但没保存
  - 说明 Python 运行的是磁盘上的文件，不是编辑器里未保存的内容

## 接下来的学习方向

下一步计划：

1. 统一当前文件命名和项目结构
2. 把 FastAPI 接口真正连上 SQLite
3. 实现文档写入数据库
4. 实现文档列表和详情接口
5. 继续推进到文件上传、向量化和 RAG

## 当前阶段的收获

目前最大的进步不只是“写了几段代码”，而是开始真正理解：

- 客户端和服务器是怎么通信的
- 数据为什么需要校验
- Python 对象、请求模型、数据库模型之间有什么区别
- 报错不是坏事，而是定位问题的线索

这个仓库不只是代码仓库，也是我目前学习过程的沉淀记录。
