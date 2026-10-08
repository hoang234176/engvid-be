# Python Type Hinting Guide for EngVid Backend

🌐 **Language / Ngôn ngữ:** **English** | [Tiếng Việt](../../vi/standards/type-hinting-guide.md)

---

This guide outlines the rules and conventions for using **Type Hints** in the `engvid-be` project. Type hints are mandatory for all production code to guarantee type safety, clarify data contracts, and enhance developer tooling.

---

## 1. Why We Enforce Type Hinting

1. **Bug Prevention:** Detects type mismatches and missing `None` checks during development instead of in production.
2. **Self-Documenting Code:** Developers can instantly understand inputs and outputs without reading internal implementations.
3. **IDE Autocompletion:** IDEs (VS Code, PyCharm, Cursor) provide accurate auto-completions and refactoring support.
4. **Framework Synergy:** Modern backend frameworks like **FastAPI** and **Pydantic** rely directly on type hints to validate payloads and generate OpenAPI/Swagger schemas.

---

## 2. Basic Type Hints

Always annotate parameters and return types for every function and method:

```python
# Basic types: int, float, str, bool, bytes
def format_user_greeting(username: str, login_count: int, is_premium: bool) -> str:
    status = "VIP" if is_premium else "Standard"
    return f"Welcome back, {username} ({status})! Total logins: {login_count}"
```

If a function does not return a value, explicitly use `None`:

```python
def log_event(event_name: str, payload: dict) -> None:
    print(f"[{event_name}] {payload}")
```

---

## 3. Modern Collection Types (Python 3.9+)

In Python 3.9+ and specifically Python 3.14+, **do not import `List`, `Dict`, `Set`, `Tuple` from the `typing` module**. Use built-in collection types directly:

```python
# Correct (Modern Python style):
def get_user_roles(user_id: str) -> list[str]:
    return ["admin", "editor"]

def get_system_config() -> dict[str, int]:
    return {"timeout": 30, "max_retries": 3}

def get_unique_tags(video_id: str) -> set[str]:
    return {"english", "grammar", "ielts"}

def get_coordinates() -> tuple[float, float]:
    return (10.762622, 106.660172)
```

```python
# Outdated (Avoid):
from typing import List, Dict, Set, Tuple

def get_user_roles(user_id: str) -> List[str]:  # Do not use typing.List
    pass
```

---

## 4. Nullable & Union Types (Python 3.10+)

Use the pipe operator (`|`) for unions and optional types. **Do not use `Optional[T]` or `Union[T, U]`**.

### Optional / Nullable Values
When a parameter or return value can be `None`:

```python
# Correct:
def find_user_by_email(email: str) -> dict[str, str] | None:
    if email == "admin@engvid.com":
        return {"id": "usr_1", "email": email}
    return None

# Avoid:
from typing import Optional
def find_user_by_email(email: str) -> Optional[dict[str, str]]:
    pass
```

### Multiple Allowed Types
```python
# Correct:
def parse_identifier(raw_id: str | int) -> str:
    return str(raw_id)
```

---

## 5. Complex Types & Aliases

### `typing.Any`
- Use `Any` sparingly, only when a variable can truly be of any type.
- Overusing `Any` defeats the purpose of type hinting.

```python
from typing import Any

def parse_arbitrary_json(data: str) -> dict[str, Any]:
    pass
```

### Type Aliases
For complex nested types, define readable type aliases:

```python
# Type aliases
VideoID = str
TimestampSeconds = float
TranscriptSegment = dict[str, TimestampSeconds | str]

def parse_subtitles(video_id: VideoID) -> list[TranscriptSegment]:
    return [{"text": "Hello world", "start": 0.0, "end": 2.5}]
```

### Callables (Functions as arguments)
```python
from collections.abc import Callable

def execute_with_retry(action: Callable[[str], bool], resource_id: str) -> bool:
    return action(resource_id)
```

---

## 6. Type Hints with Classes & Models

For structured backend requests and responses, use **Pydantic models**:

```python
from pydantic import BaseModel, Field

class VideoCreateRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None
    duration_seconds: int = Field(..., gt=0)
    tags: list[str] = []

class VideoResponse(BaseModel):
    id: str
    title: str
    url: str
```

---

## 7. Static Type Checking

Before pushing code, verify type consistency using `mypy` or `pyright`:

```bash
# Check static types
mypy .
```
