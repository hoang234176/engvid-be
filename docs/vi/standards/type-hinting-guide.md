# Hướng Dẫn Sử Dụng Type Hinting Cho EngVid Backend

🌐 **Language / Ngôn ngữ:** [English](../../en/standards/type-hinting-guide.md) | **Tiếng Việt**

---

Tài liệu này quy định việc sử dụng **Gợi ý kiểu dữ liệu (Type Hints)** trong dự án `engvid-be`. Type hints là quy định bắt buộc cho toàn bộ mã nguồn nhằm đảm bảo an toàn kiểu dữ liệu, giảm thiểu bug và tối ưu trải nghiệm lập trình.

---

## 1. Vì Sao Bắt Buộc Sử Dụng Type Hinting?

1. **Phát hiện lỗi sớm:** Tìm ra lỗi sai kiểu dữ liệu hoặc xử lý thiếu trường hợp `None` ngay khi viết code, thay vì để lỗi xảy ra trên môi trường chạy thực tế.
2. **Code tự làm tài liệu (Self-Documenting):** Đọc khai báo hàm là hiểu ngay cần truyền dữ liệu gì vào và nhận về kết quả gì mà không cần đọc hết code logic bên trong.
3. **Gợi ý code thông minh từ IDE:** Các IDE (VS Code, PyCharm, Cursor) tự động hoàn thành code (autocomplete) chính xác tuyệt đối.
4. **Tích hợp hoàn hảo với Framework:** Các framework backend hiện đại như **FastAPI** và **Pydantic** dựa hoàn toàn vào Type Hinting để tự động validate dữ liệu đầu vào và tự sinh tài liệu API (Swagger UI).

---

## 2. Type Hinting Cơ Bản

Luôn khai báo kiểu cho tất cả tham số hàm và giá trị trả về:

```python
# Các kiểu cơ bản: int, float, str, bool, bytes
def format_user_greeting(username: str, login_count: int, is_premium: bool) -> str:
    status = "VIP" if is_premium else "Thường"
    return f"Chào mừng {username} ({status})! Số lần đăng nhập: {login_count}"
```

Nếu hàm không trả về giá trị, ghi rõ `None`:

```python
def log_event(event_name: str, payload: dict) -> None:
    print(f"[{event_name}] {payload}")
```

---

## 3. Kiểu Dữ Liệu Tập Hợp Hiện Đại (Python 3.9+)

Trên Python 3.9+ và đặc biệt là phiên bản Python 3.14+, **không import `List`, `Dict`, `Set`, `Tuple` từ thư viện `typing`**. Hãy sử dụng trực tiếp các kiểu tích hợp sẵn của Python:

```python
# Đúng (Chuẩn Python hiện đại):
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
# Cũ (Tránh dùng):
from typing import List, Dict, Set, Tuple

def get_user_roles(user_id: str) -> List[str]:  # Không dùng List từ typing nữa
    pass
```

---

## 4. Xử Lý Giá Trị Nullable & Kiểu Hợp (Python 3.10+)

Sử dụng toán tử gạch đứng (`|`) để biểu thị các kiểu dữ liệu có thể nhận giá trị `None` hoặc nhiều kiểu khác nhau. **Không dùng `Optional[T]` hoặc `Union[T, U]`**.

### Dữ Liệu Có Thể Là `None`
```python
# Đúng:
def find_user_by_email(email: str) -> dict[str, str] | None:
    if email == "admin@engvid.com":
        return {"id": "usr_1", "email": email}
    return None

# Tránh:
from typing import Optional
def find_user_by_email(email: str) -> Optional[dict[str, str]]:
    pass
```

### Biến Có Thể Thuộc Nhiều Kiểu Khác Nhau
```python
# Đúng:
def parse_identifier(raw_id: str | int) -> str:
    return str(raw_id)
```

---

## 5. Các Kiểu Phức Tạp & Định Danh Kiểu (Type Aliases)

### `typing.Any`
- Chỉ dùng `Any` khi dữ liệu thực sự hoàn toàn không xác định được kiểu.
- Lạm dụng `Any` sẽ làm mất đi ý nghĩa của Type Hinting.

```python
from typing import Any

def parse_arbitrary_json(data: str) -> dict[str, Any]:
    pass
```

### Type Aliases (Đặt tên gợi nhớ cho kiểu phức tạp)
```python
# Type aliases
VideoID = str
TimestampSeconds = float
TranscriptSegment = dict[str, TimestampSeconds | str]

def parse_subtitles(video_id: VideoID) -> list[TranscriptSegment]:
    return [{"text": "Hello world", "start": 0.0, "end": 2.5}]
```

### Callables (Hàm truyền vào như tham số)
```python
from collections.abc import Callable

def execute_with_retry(action: Callable[[str], bool], resource_id: str) -> bool:
    return action(resource_id)
```

---

## 6. Type Hints Với Class & Pydantic Model

Đối với dữ liệu đầu vào/đầu ra của backend API, ưu tiên dùng **Pydantic models**:

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

## 7. Kiểm Tra Kiểu Tĩnh (Static Type Checking)

Code bắt buộc phải vượt qua bước kiểm tra kiểu trước khi merge PR:

```bash
# Kiểm tra kiểu bằng mypy
mypy .
```
