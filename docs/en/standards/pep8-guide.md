# PEP 8 Style Guide for EngVid Backend

🌐 **Language / Ngôn ngữ:** **English** | [Tiếng Việt](../../vi/standards/pep8-guide.md)

---

> **Note on "PEP 8":** The number **8** in PEP 8 does not mean there are only 8 rules. It refers to **Python Enhancement Proposal #8**, submitted in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. It is the comprehensive official style guide for Python code.

This document outlines the essential conventions adapted from PEP 8 for the `engvid-be` project.

---

## 1. Code Layout & Formatting

### Indentation
- Use strictly **4 spaces** per indentation level.
- **Never use tabs**. Configure your editor to insert spaces on tab keypress.

```python
# Correct:
def calculate_video_duration(segments: list[int]) -> int:
    total_duration = 0
    for segment in segments:
        total_duration += segment
    return total_duration

# Incorrect:
def calculate_video_duration(segments: list[int]) -> int:
  total_duration = 0 # 2 spaces - avoid
	for segment in segments: # Tab used - strictly forbidden
		total_duration += segment
	return total_duration
```

### Maximum Line Length
- Standard maximum line length is **88 to 100 characters** (compatible with modern formatters like Black and Ruff).
- Wrap long lines using parentheses instead of backslashes (`\`).

```python
# Correct:
from app.services.video_processing import (
    transcode_video_stream,
    generate_subtitles_with_timestamp,
)

# Avoid:
from app.services.video_processing import transcode_video_stream, generate_subtitles_with_timestamp
```

### Blank Lines
- Separate top-level function and class definitions with **two blank lines**.
- Separate method definitions inside a class with **a single blank line**.
- Use blank lines sparingly inside functions to separate logical blocks.

```python
class VideoProcessor:
    """Handles video processing and transcoding."""

    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def process_file(self, filename: str) -> bool:
        if not filename:
            return False

        return True


def helper_function() -> None:
    pass
```

### Imports Order & Grouping
Imports must always be placed at the very top of the file, divided into three distinct groups separated by a blank line:
1. **Standard library imports**
2. **Third-party library imports**
3. **Local application imports**

```python
# Correct:
import os
import sys
from datetime import datetime

import httpx
from pydantic import BaseModel

from app.core.config import settings
from app.services.storage import StorageService
```

---

## 2. Whitespace in Expressions

### Avoid Extraneous Whitespace
- Avoid spaces immediately inside brackets, braces, or parentheses.
- Avoid spaces before commas, colons, or semicolons.

```python
# Correct:
user_ids = [1, 2, 3]
profile = {"username": "hoang", "role": "admin"}
result = calculate(user_ids[0], 42)

# Incorrect:
user_ids = [ 1, 2, 3 ]
profile = { "username" : "hoang" , "role" : "admin" }
result = calculate( user_ids[ 0 ], 42 )
```

### Binary Operators
- Always surround binary operators with a single space: `=`, `+=`, `==`, `<`, `>`, `and`, `or`, etc.
- **Do not** use spaces around the `=` sign for keyword arguments or default parameter values.

```python
# Correct:
count = 10
is_active = (count > 0) and True

def fetch_data(timeout: int = 30) -> dict:
    return {}

# Incorrect:
count=10
def fetch_data(timeout: int = 30) -> dict:
    return {}
```

---

## 3. Naming Conventions

Follow these casing rules consistently across the codebase:

| Target | Convention | Example |
| :--- | :--- | :--- |
| **Modules / Files** | `snake_case` | `video_processor.py`, `auth_service.py` |
| **Packages / Directories** | `snake_case` | `services/`, `core/`, `api_v1/` |
| **Classes / Exceptions** | `PascalCase` | `UserService`, `VideoNotFoundError` |
| **Functions & Methods** | `snake_case` | `get_user_by_id()`, `process_video()` |
| **Variables & Attributes** | `snake_case` | `user_token`, `file_size`, `is_active` |
| **Constants** | `UPPER_SNAKE_CASE` | `MAX_FILE_SIZE_MB`, `DEFAULT_PAGE_LIMIT` |
| **Private Attributes/Methods** | `_leading_underscore` | `_internal_cache`, `_hash_password()` |

---

## 4. Programming Recommendations & Best Practices

- **Comparisons to Singletons:** Always use `is` or `is not` when comparing to `None` or boolean singletons.
  ```python
  # Correct:
  if user is None:
      ...
  
  # Incorrect:
  if user == None:
      ...
  ```
- **Boolean checks:** Do not compare boolean variables to `True` or `False` using `==`.
  ```python
  # Correct:
  if is_authenticated:
      ...

  # Incorrect:
  if is_authenticated == True:
      ...
  ```
- **Exception handling:** Always catch specific exceptions; avoid bare `except:` or catching generic `Exception` without re-raising.
  ```python
  # Correct:
  try:
      value = int(payload["age"])
  except (KeyError, ValueError) as err:
      logger.error("Invalid age payload: %s", err)
      raise

  # Incorrect:
  try:
      value = int(payload["age"])
  except:
      pass
  ```

---

## 5. Automated Formatting & Linting

Before pushing code, run automated tools to ensure PEP 8 compliance:
```bash
# Recommended: Using Ruff (Fast and comprehensive)
ruff format .
ruff check . --fix
```
