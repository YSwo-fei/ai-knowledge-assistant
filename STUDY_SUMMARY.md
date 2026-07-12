# Study Summary

## Purpose

This file is a compact review sheet for the current stage of learning.

## Python Basics

- Variable assignment uses `=`
- Comparison uses `==`, `<`, `>`, `<=`, `>=`
- Strings must be wrapped in quotes
- Python uses indentation instead of braces

Example:

```python
name = "feiyuai"
age = 18

if age >= 18:
    print("adult")
```

## Common Structures

### List

```python
items = ["a", "b", "c"]
items[0]
len(items)
```

### Dict

```python
data = {"name": "feiyuai"}
data["name"]
data.get("age", 0)
```

## File Operations

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

## Git Review

- `git add`: stage changes
- `git commit`: create a local snapshot
- `git push`: upload to GitHub

## FastAPI Review

### GET

Used to fetch data from the server.

### POST

Used to send data to the server.

### Pydantic

`BaseModel` is used to define request data format.

```python
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    context: str
```

## `422` Meaning

`422 Unprocessable Content` means:

- the request reached the server
- but the body data does not match the expected schema

Typical reasons:

- missing field
- wrong field name
- wrong field type

## Current Practical Files

- `todo.py`
- `work.py`
- `main.py`
- `schemy.py`
- `model.py`
- `datebase.py`

## Current Focus

The current learning focus is:

1. understand FastAPI request handling
2. connect request models to database models
3. build document CRUD step by step
