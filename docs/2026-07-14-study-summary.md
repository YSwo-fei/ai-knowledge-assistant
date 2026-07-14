# 2026-07-14 学习复盘：FastAPI + 数据库 CRUD 基础

## 1. 今天学习目标

今天的主线是：把一个后端项目从“能启动”推进到“能连接数据库并实现基础 CRUD”。

当前项目目标是 AI 知识库助手。后面真正做 RAG、文档问答、大模型接入之前，必须先把后端基础打牢：

- 会写 FastAPI 接口
- 会区分 GET、POST、PUT、PATCH、DELETE
- 会定义请求数据模型
- 会定义数据库表模型
- 会连接 SQLite 数据库
- 会通过 SQLAlchemy 操作数据库
- 会把接口逻辑拆分到不同文件中

## 2. 当前项目文件分工

目前后端代码开始从“全部写在一个文件”过渡到“分层结构”。

| 文件 | 作用 |
| --- | --- |
| `main.py` | 项目入口，创建 FastAPI 应用，注册路由，初始化数据库 |
| `datebase.py` | 数据库连接、Session 创建、Base 定义、初始化表 |
| `model.py` | 数据库表模型，例如 `Document` 表 |
| `schemy.py` | 请求和响应的数据格式校验模型 |
| `crud.py` | 专门写数据库增删改查逻辑 |
| `rounters/document.py` | 专门写文档相关 API 路由 |

后面建议逐步把拼写修正为更标准的命名：

- `datebase.py` 改为 `database.py`
- `schemy.py` 改为 `schemas.py`
- `rounters` 改为 `routers`

当前阶段先保证能理解和跑通，不急着做大规模重命名。

## 3. FastAPI 基础复盘

FastAPI 是一个 Python 后端框架。它的核心工作是：

1. 接收浏览器、Swagger、前端或其他客户端发来的 HTTP 请求
2. 根据请求路径找到对应函数
3. 执行函数里的业务逻辑
4. 返回 JSON 数据

示例：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}
```

这段代码的含义：

- `app = FastAPI()` 创建后端应用
- `@app.get("/")` 注册一个 GET 接口
- 用户访问 `/` 时，FastAPI 会调用 `home()`
- `return {"message": "hello"}` 会被自动转成 JSON 返回

## 4. HTTP 方法区别

HTTP 方法可以理解为“用户想对资源做什么操作”。

| 方法 | 作用 | CRUD 对应 |
| --- | --- | --- |
| GET | 查询数据 | Read |
| POST | 创建新数据 | Create |
| PUT | 整体更新数据 | Update |
| PATCH | 局部更新数据 | Update |
| DELETE | 删除数据 | Delete |

### GET

GET 用于获取数据。

例如：

```http
GET /api/documents
```

意思是：查询文档列表。

### POST

POST 用于提交数据并创建资源。

例如：

```http
POST /api/documents
```

请求体：

```json
{
  "title": "Python 基础",
  "content": "Python 是一门编程语言",
  "file_type": "text"
}
```

意思是：新增一篇文档。

### PUT

PUT 通常用于整体替换。

例如数据库里已有：

```json
{
  "title": "旧标题",
  "content": "旧内容",
  "file_type": "text"
}
```

PUT 更新时通常要求把完整对象都发过去。

### PATCH

PATCH 用于局部更新。

例如只改标题：

```json
{
  "title": "新标题"
}
```

没有传的字段保持原样。

### DELETE

DELETE 用于删除数据。

例如：

```http
DELETE /api/documents/3
```

意思是：删除 ID 为 3 的文档。

## 5. 数据库基础复盘

数据库是专门用来长期保存数据的系统。

普通变量只存在于程序运行期间，程序关闭后就没了。数据库里的数据会写到磁盘上，程序重启后还能继续读取。

### 表、行、列

可以把数据库表想象成 Excel 表格：

| id | title | content |
| --- | --- | --- |
| 1 | Python | Python 基础内容 |
| 2 | FastAPI | FastAPI 基础内容 |

对应关系：

- 表：一类数据的集合，例如 `documents`
- 行：一条具体记录
- 列：一个字段，例如 `title`
- 主键：唯一标识一条记录的字段，通常是 `id`

## 6. SQLAlchemy 基础

SQLAlchemy 是 Python 操作数据库的工具。

它可以让我们少写 SQL，用 Python 类来表示数据库表。

### Base

```python
Base = declarative_base()
```

`Base` 是所有数据库模型类的父类。

数据库模型要继承它：

```python
class Document(Base):
    __tablename__ = "documents"
```

意思是：`Document` 这个 Python 类对应数据库中的 `documents` 表。

### engine

```python
engine = create_engine("sqlite:///data/app.db", echo=False)
```

`engine` 表示数据库连接引擎。

可以理解为：Python 程序连接数据库的通道。

### SessionLocal

```python
SessionLocal = sessionmaker(bind=engine)
```

`SessionLocal` 用来创建数据库会话。

一次请求通常创建一个 `db`：

```python
db = SessionLocal()
```

然后通过 `db` 去查、增、改、删数据库。

## 7. 数据库操作关键词

### add

```python
db.add(document)
```

把一个新对象加入数据库会话。

注意：这时还没有真正写入数据库。

### commit

```python
db.commit()
```

真正提交到数据库。

没有 `commit()`，数据通常不会最终保存。

### refresh

```python
db.refresh(document)
```

从数据库重新读取这个对象。

常见用途：拿到数据库自动生成的 `id`。

### rollback

```python
db.rollback()
```

如果提交失败，就撤销这次未完成的操作。

### close

```python
db.close()
```

关闭数据库会话。

## 8. 请求模型和数据库模型的区别

这是今天非常重要的概念。

### 请求模型

请求模型写在 `schemy.py` 里，继承 `BaseModel`。

它负责校验用户发来的数据。

示例：

```python
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    content: str
    file_type: str = "text"
```

如果用户不发送 `title`，FastAPI 会返回 `422`。

如果用户不发送 `file_type`，默认值是 `"text"`。

### 数据库模型

数据库模型写在 `model.py` 里，继承 `Base`。

它负责描述数据库表结构。

示例：

```python
class Document(Base):
    __tablename__ = "documents"
```

### 为什么不能混用

请求模型面对的是“用户请求”。

数据库模型面对的是“数据库表”。

它们职责不同，所以要分开。

## 9. 422 错误

`422 Unprocessable Content` 表示：

请求已经到达后端，但请求体内容不符合后端模型要求。

常见原因：

- 缺少必填字段
- 字段名写错
- 字段类型不对
- 后端模型叫 `content`，但前端发送了 `context`

例如后端要求：

```python
class DocumentCreate(BaseModel):
    title: str
    content: str
```

但用户发送：

```json
{
  "title": "测试",
  "context": "内容"
}
```

这就会报 422，因为后端要的是 `content`，不是 `context`。

## 10. 500 错误

`500 Internal Server Error` 表示：

请求到达后端了，但后端代码运行时崩了。

今天遇到的典型错误：

```text
sqlite3.OperationalError: unable to open database file
```

原因通常是 SQLite 数据库路径所在的目录不存在。

例如：

```python
sqlite:///data/app.db
```

如果 `data` 文件夹不存在，SQLite 无法创建 `app.db`。

解决思路是在初始化数据库前创建目录：

```python
os.makedirs("data", exist_ok=True)
```

## 11. CRUD 分层思路

CRUD 是四类基础操作：

- Create：创建
- Read：读取
- Update：更新
- Delete：删除

项目里建议拆成三层：

| 层 | 文件 | 职责 |
| --- | --- | --- |
| API 层 | `rounters/document.py` | 接收 HTTP 请求，返回 HTTP 响应 |
| CRUD 层 | `crud.py` | 操作数据库 |
| Model 层 | `model.py` | 定义数据库表 |

这样做的原因：

- 路由文件不会越来越乱
- 数据库操作可以复用
- 后面加测试更方便
- 项目结构更接近真实工作项目

## 12. 查询和分页

今天写过的查询逻辑大概是：

```python
def get_documents(db, keyword=None, page=1, page_size=20):
    query = db.query(Document)

    if keyword:
        query = query.filter(Document.title.contains(keyword))

    total = query.count()

    documents = (
        query
        .order_by(Document.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return total, documents
```

含义：

- `keyword` 用于搜索
- `page` 表示第几页
- `page_size` 表示每页多少条
- `count()` 统计总数
- `offset()` 跳过前面的数据
- `limit()` 限制返回数量
- `order_by(Document.id.desc())` 按最新数据排在前面

### 为什么用户不需要知道 ID

用户通常不会直接知道数据库 ID。

真实流程是：

1. 用户输入关键词
2. 后端返回匹配的文档列表
3. 每条文档内部都有 `id`
4. 前端展示标题，但内部保存 `id`
5. 用户点击某条文档时，前端拿对应 `id` 去请求详情

所以 ID 不一定展示给用户，但系统内部必须使用 ID。

## 13. 今天常见拼写问题

这些问题不是能力问题，而是初学阶段最常见的问题。要养成逐字检查的习惯。

| 错误 | 正确 |
| --- | --- |
| `BaseModelc` | `BaseModel` |
| `pytjon-dotenv` | `python-dotenv` |
| `eho=False` | `echo=False` |
| `context` / `content` 混用 | 前后端字段名保持一致 |
| `datebase` | 建议以后改成 `database` |
| `schemy` | 建议以后改成 `schemas` |
| `rounters` | 建议以后改成 `routers` |

## 14. Git 复盘

Git 的核心流程：

```bash
git status
git add .
git commit -m "message"
git push origin main
```

含义：

- `git status` 查看当前改动
- `git add` 加入暂存区
- `git commit` 生成一次本地提交
- `git push` 推送到 GitHub

可以这样理解：

- `add`：把改动放到准备提交的篮子里
- `commit`：把篮子里的内容打包成一个版本
- `push`：把本地版本上传到 GitHub

## 15. 当前阶段下一步

下一次继续时，建议按这个顺序推进：

1. 先把当前 CRUD 接口全部在 `/docs` 里测一遍
2. 测试 POST 创建文档
3. 测试 GET 查询文档列表
4. 测试 GET 根据 ID 查询详情
5. 测试 PATCH 修改文档
6. 测试 DELETE 删除文档
7. 修正命名：`database.py`、`schemas.py`、`routers`
8. 解决中文乱码问题，保证所有文件保存为 UTF-8
9. 给每个接口加清晰的返回模型
10. 再进入文档上传和 AI 问答

## 16. 今天的核心结论

今天最重要的不是记住所有语法，而是建立后端项目的基本思维：

1. 用户通过 HTTP 请求访问接口
2. FastAPI 根据路由找到函数
3. Pydantic 校验请求数据
4. CRUD 层操作数据库
5. SQLAlchemy 把 Python 对象转换成数据库记录
6. 数据最终保存到 SQLite 文件中
7. 后端把处理结果返回给用户

这条链路理解清楚，后面接 AI、接 RAG、接前端，都是在这条基础链路上继续加功能。
