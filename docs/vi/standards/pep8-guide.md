# Hướng Dẫn Phong Cách Viết Code PEP 8 cho EngVid Backend

🌐 **Language / Ngôn ngữ:** [English](../../en/standards/pep8-guide.md) | **Tiếng Việt**

---

> **Lưu ý về tên gọi "PEP 8":** Con số **8** trong PEP 8 không có nghĩa là chỉ có 8 quy tắc. Đây là mã số văn bản **Python Enhancement Proposal số 8**, được đề xuất từ năm 2001 bởi Guido van Rossum, Barry Warsaw và Nick Coghlan. Đây là bộ quy chuẩn phong cách lập trình chính thức và đầy đủ nhất cho ngôn ngữ Python.

Tài liệu này tổng hợp các quy tắc cốt lõi từ PEP 8 được áp dụng cho dự án `engvid-be`.

---

## 1. Định Dạng & Bố Cục Mã Nguồn (Code Layout)

### Thụt Lề (Indentation)
- Sử dụng chính xác **4 dấu cách (spaces)** cho mỗi cấp thụt lề.
- **Tuyệt đối không dùng phím Tab**. Hãy cấu hình editor/IDE tự động đổi phím Tab thành 4 dấu cách.

```python
# Đúng:
def calculate_video_duration(segments: list[int]) -> int:
    total_duration = 0
    for segment in segments:
        total_duration += segment
    return total_duration

# Sai:
def calculate_video_duration(segments: list[int]) -> int:
  total_duration = 0 # Thụt 2 dấu cách - tránh
	for segment in segments: # Dùng phím Tab - nghiêm cấm
		total_duration += segment
	return total_duration
```

### Độ Dài Tối Đa Của Một Dòng
- Độ dài tối đa chuẩn cho mỗi dòng là **88 đến 100 ký tự** (tương thích với các công cụ format hiện đại như Black và Ruff).
- Bẻ dòng dài bằng dấu ngoặc tròn `()`, hạn chế tối đa việc dùng dấu gạch chéo ngược (`\`).

```python
# Đúng:
from app.services.video_processing import (
    transcode_video_stream,
    generate_subtitles_with_timestamp,
)

# Tránh viết 1 dòng quá dài:
from app.services.video_processing import transcode_video_stream, generate_subtitles_with_timestamp
```

### Dòng Trống (Blank Lines)
- Phân tách giữa các hàm và các class cấp cao nhất bằng **2 dòng trống**.
- Phân tách các phương thức (methods) bên trong một class bằng **1 dòng trống**.
- Dùng các dòng trống bên trong thân hàm một cách hợp lý để ngăn cách các khối logic khác nhau.

```python
class VideoProcessor:
    """Xử lý và chuyển đổi định dạng video."""

    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def process_file(self, filename: str) -> bool:
        if not filename:
            return False

        return True


def helper_function() -> None:
    pass
```

### Thứ Tự & Gom Nhóm Thư Viện Import
Các câu lệnh `import` luôn đặt ở đầu file, chia thành 3 nhóm rõ ràng phân cách nhau bằng một dòng trống:
1. **Thư viện chuẩn của Python (Standard library)**
2. **Thư viện bên thứ ba (Third-party packages)**
3. **Các module nội bộ của dự án (Local imports)**

```python
# Đúng:
import os
import sys
from datetime import datetime

import httpx
from pydantic import BaseModel

from app.core.config import settings
from app.services.storage import StorageService
```

---

## 2. Khoảng Trắng Trong Biểu Thức

### Tránh Khoảng Trắng Thừa
- Không đặt dấu cách ngay bên trong dấu ngoặc vuông `[]`, ngoặc nhọn `{}` hay ngoặc tròn `()`.
- Không đặt dấu cách trước dấu phẩy, dấu hai chấm hoặc dấu chấm phẩy.

```python
# Đúng:
user_ids = [1, 2, 3]
profile = {"username": "hoang", "role": "admin"}
result = calculate(user_ids[0], 42)

# Sai:
user_ids = [ 1, 2, 3 ]
profile = { "username" : "hoang" , "role" : "admin" }
result = calculate( user_ids[ 0 ], 42 )
```

### Toán Tử Hai Ngôi (Binary Operators)
- Luôn đặt 1 dấu cách ở cả hai phía của toán tử: `=`, `+=`, `==`, `<`, `>`, `and`, `or`, v.v.
- **Không** đặt khoảng trắng quanh dấu `=` khi khai báo giá trị mặc định cho tham số của hàm.

```python
# Đúng:
count = 10
is_active = (count > 0) and True

def fetch_data(timeout: int = 30) -> dict:
    return {}

# Sai:
count=10
def fetch_data(timeout: int=30) -> dict:
    return {}
```

---

## 3. Quy Ước Đặt Tên (Naming Conventions)

Tuân thủ nghiêm ngặt quy tắc đặt tên trong toàn bộ dự án:

| Đối tượng | Quy ước | Ví dụ |
| :--- | :--- | :--- |
| **Modules / Tên File** | `snake_case` | `video_processor.py`, `auth_service.py` |
| **Packages / Thư mục** | `snake_case` (ngắn gọn) | `services/`, `core/`, `api_v1/` |
| **Classes / Exceptions** | `PascalCase` | `UserService`, `VideoNotFoundError` |
| **Hàm & Phương thức** | `snake_case` | `get_user_by_id()`, `process_video()` |
| **Biến & Thuộc tính** | `snake_case` | `user_token`, `file_size`, `is_active` |
| **Hằng số (Constants)** | `UPPER_SNAKE_CASE` | `MAX_FILE_SIZE_MB`, `DEFAULT_PAGE_LIMIT` |
| **Thuộc tính/Hàm nội bộ (Private)** | `_dấu_gạch_dưới_ở_đầu` | `_internal_cache`, `_hash_password()` |

---

## 4. Khuyến Nghị Lập Trình & Best Practices

- **So sánh với Singleton:** Luôn dùng `is` hoặc `is not` khi kiểm tra biến với `None` hoặc giá trị boolean đơn lẻ.
  ```python
  # Đúng:
  if user is None:
      ...
  
  # Sai:
  if user == None:
      ...
  ```
- **Kiểm tra Boolean:** Không so sánh biến boolean với `True` hoặc `False` bằng toán tử `==`.
  ```python
  # Đúng:
  if is_authenticated:
      ...

  # Sai:
  if is_authenticated == True:
      ...
  ```
- **Xử lý Ngoại lệ (Exception Handling):** Luôn bắt ngoại lệ cụ thể, không dùng `except:` trống trơn hoặc bắt `Exception` chung chung mà không re-raise.
  ```python
  # Đúng:
  try:
      value = int(payload["age"])
  except (KeyError, ValueError) as err:
      logger.error("Dữ liệu tuổi không hợp lệ: %s", err)
      raise

  # Sai:
  try:
      value = int(payload["age"])
  except:
      pass
  ```

---

## 5. Tự Động Định Dạng & Kiểm Tra Lỗi

Trước khi commit/push code, hãy chạy công cụ kiểm tra tự động:
```bash
# Khuyến nghị: Sử dụng Ruff (Cực nhanh và chính xác)
ruff format .
ruff check . --fix
```
