# AI Knowledge Assistant Learning Notes

This repository records my early-stage learning and practice while building toward an AI knowledge assistant project.

## Current Stage

We are in the transition from Python basics to backend development with FastAPI.

Completed so far:

- Python basics: variables, conditions, loops, functions
- Common data structures: list and dict
- File reading and writing
- Basic Git workflow
- AI-assisted coding with a CLI todo app
- FastAPI first steps: routes, request models, and debugging `422` errors

## Files In This Repository

- `todo.py`: command-line todo application with JSON persistence
- `todo.json`: sample persisted todo data
- `work.py`: word frequency counting practice
- `main.py`: current FastAPI practice entry file
- `schemy.py`: current Pydantic request model practice file
- `model.py`: current SQLAlchemy model practice file
- `datebase.py`: current database connection practice file

Note:

- Some filenames are intentionally kept as-is because they reflect the current learning state.
- A few names are not yet standardized, such as `datebase.py`, `schemy.py`, and `requirement.txt`.
- These will be cleaned up in the next refactor step after the learning concepts are stable.

## What I Learned

### 1. Python Basics

Important ideas:

- Variables store data
- Strings need quotes
- `if / else` controls branching
- `for` and `while` control repetition
- `def` defines a function
- Indentation is part of Python syntax

Example:

```python
age = 16

if age >= 18:
    print("adult")
else:
    print("minor")
```

### 2. List and Dict

List is used to store ordered data:

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(len(fruits))
```

Dict is used for key-value storage:

```python
student = {"name": "feiyuai", "age": 22}
print(student["name"])
```

### 3. File Reading and Writing

Reading a file:

```python
with open("a.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

Writing a file:

```python
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

### 4. Word Count Practice

`work.py` reads a file, splits words, then counts frequency with a dict.

Core idea:

```python
count[word] = count.get(word, 0) + 1
```

This means:

- if the word already exists, increase its count
- if it does not exist, start from `0`

### 5. Git Basics

The basic workflow:

```bash
git status
git add .
git commit -m "message"
git push
```

Key distinction:

- `git add`: move changes into the staging area
- `git commit`: create a local snapshot
- `git push`: upload the snapshot to GitHub

### 6. AI-Assisted Coding

I used AI to help generate a practical todo app.

What mattered most was not blindly copying code, but understanding:

- what each function does
- where data is stored
- how command-line arguments are passed in
- how to read errors and fix them

### 7. FastAPI First Contact

Basic route example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}
```

FastAPI is used to build APIs. Compared with earlier Flask practice, it gives us:

- automatic request parsing
- automatic type validation
- automatic docs page at `/docs`

### 8. Pydantic Request Models

Example:

```python
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    context: str
    file_size: int = 0
    file_type: str = "text"
```

This model defines what the client must send.

Important ideas:

- fields without defaults are required
- fields with defaults are optional
- FastAPI converts JSON into an object automatically

That is why code like this works:

```python
document.title
```

Because `document` is already an object created from the request body.

### 9. Why `422 Unprocessable Content` Happens

This error means:

- the request reached the server
- but the JSON body does not match the expected model

Common causes:

- missing required field
- wrong field name
- wrong field type

Example:

If the model expects:

```json
{
  "title": "test",
  "context": "body text"
}
```

but you send:

```json
{
  "title": "test",
  "content": "body text"
}
```

then FastAPI returns `422`.

### 10. GET vs POST

Simple memory rule:

- `GET`: ask the server for data
- `POST`: send data to the server

Examples:

- opening `/api/info` is usually `GET`
- creating a document is usually `POST`

## Current Code State

The project is still in a learning state and not yet refactored.

Known issues still present:

- naming is inconsistent:
  - `datebase.py` should later become `database.py`
  - `schemy.py` should later become `schemas.py`
  - `model.py` should later become `models.py`
  - `requirement.txt` should later become `requirements.txt`
- some Chinese text in files is garbled because of encoding issues during editing
- `main.py` is still a learning prototype, not yet a full project skeleton
- database persistence for documents is not fully connected yet

This is normal for the current stage. The goal right now is understanding concepts first, then standardizing structure.

## Main Bugs We Solved

Examples of real mistakes and what they taught me:

- `BaseModelc` vs `BaseModel`
  - import names must be exact
- `eho=False` vs `echo=False`
  - keyword arguments must be spelled exactly
- `content` vs `context`
  - request model field names must match the data actually sent
- `git add` vs `git commit`
  - staging and committing are different steps
- unsaved file changes in the editor
  - running code uses the saved file on disk, not the unsaved editor buffer

## Next Steps

Planned next learning steps:

1. Standardize filenames and project structure
2. Connect FastAPI route to SQLite through SQLAlchemy
3. Implement real document creation in the database
4. Add document listing and retrieval APIs
5. Move toward file upload, vectorization, and RAG

## Short Reflection

The biggest progress so far is not just writing code, but starting to understand:

- how client and server communicate
- how data is validated
- how Python objects, request models, and database models are different
- how to read errors instead of fearing them

This repository is both a codebase and a learning record.
