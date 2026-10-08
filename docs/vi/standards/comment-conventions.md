# Quy Ước Viết Comment Code Cho EngVid Backend

🌐 **Language / Ngôn ngữ:** [English](../../en/standards/comment-conventions.md) | **Tiếng Việt**

---

Comment code rõ ràng, đúng mục đích giúp codebase dễ tiếp cận, dễ bảo trì và hạn chế tối đa lỗi ngầm khi cộng tác. Tài liệu này quy định tiêu chuẩn viết comment cho dự án `engvid-be`.

---

## 1. Nguyên Tắc Cốt Lõi

### Ngôn Ngữ
- **Toàn bộ comment và docstrings trong code bắt buộc phải viết bằng Tiếng Anh.**

### Giải Thích "Tại Sao" (Why), Không Phải "Cái Gì" (What)
- Bản thân code đã thể hiện *cái gì* đang chạy (thông qua cách đặt tên biến, hàm rõ ràng).
- Comment chỉ dùng để giải thích **lý do nghiệp vụ**, **ràng buộc ngầm**, **trường hợp ngoại lệ (edge case)** hoặc **giải pháp tình thế (workaround)**.

```python
# Sai (Chỉ nhắc lại cú pháp hiển nhiên):
# tăng counter lên 1
counter += 1

# Đúng (Giải thích lý do đằng sau):
# ffmpeg segment indexing requires 1-based indexing for stream compatibility
counter += 1
```

### Luôn Cập Nhật Comment Cùng Với Code
- Một comment sai hoặc lỗi thời còn nguy hiểm hơn việc không có comment. Khi sửa logic, hãy sửa hoặc xóa comment cũ ngay lập tức.

### Nghiêm Cấm Commit "Code Bị Comment" (Dead Code)
- **Tuyệt đối không commit các khối code bị comment lại.**
- Git đã lưu trữ toàn bộ lịch sử thay đổi. Nếu đoạn code không còn dùng nữa, hãy xóa hẳn.

---

## 2. Quy Chuẩn Docstrings (PEP 257 & Google Style)

Tất cả các module, class, method và function public đều phải có docstring dạng ba dấu ngoặc kép (`"""..."""`). Dự án áp dụng theo định dạng **Google Python Style**.

### Định Dạng Docstring Cho Hàm / Phương Thức

```python
def transcode_video(
    source_path: str,
    target_resolution: str,
    bitrate_kbps: int = 1500,
) -> str:
    """Chuyển đổi file video đầu vào sang độ phân giải mục tiêu.

    Thực thi tiến trình phụ ffmpeg bất đồng bộ để mã hóa lại video gốc
    trong khi vẫn giữ nguyên chất lượng các kênh âm thanh.

    Args:
        source_path: Đường dẫn tuyệt đối đến file video gốc.
        target_resolution: Chuỗi độ phân giải (ví dụ: '1080p', '720p').
        bitrate_kbps: Giới hạn bitrate tính bằng kilobits/giây. Mặc định là 1500.

    Returns:
        Đường dẫn tuyệt đối đến file video đã chuyển đổi thành công.

    Raises:
        FileNotFoundError: Nếu `source_path` không tồn tại trên ổ đĩa.
        TranscodingError: Nếu ffmpeg gặp lỗi trong quá trình chuyển đổi luồng.
    """
    # Triển khai hàm...
```

### Định Dạng Docstring Cho Class

```python
class StorageService:
    """Quản lý lưu trữ file lên ổ đĩa cục bộ và dịch vụ đám mây chuẩn S3.

    Attributes:
        bucket_name: Tên bucket đám mây phục vụ phân phối tài nguyên công khai.
        cache_dir: Thư mục tạm cục bộ chứa các file đang trong tiến trình upload.
    """

    def __init__(self, bucket_name: str, cache_dir: str) -> None:
        self.bucket_name = bucket_name
        self.cache_dir = cache_dir
```

---

## 3. Các Thẻ Ghi Chú Hành Động (Action Tags)

Khi cần để lại ghi chú nhanh trong code, sử dụng các tiền tố chuẩn sau (viết hoa toàn bộ):

| Thẻ | Ý nghĩa | Cách dùng |
| :--- | :--- | :--- |
| `TODO:` | Việc cần làm | Đánh dấu tính năng hoặc việc tối ưu dự kiến triển khai sau. |
| `FIXME:` | Lỗi đã biết | Nêu rõ lỗi hoặc rủi ro cần được ưu tiên khắc phục sớm. |
| `NOTE:` | Lưu ý quan trọng | Giải thích ngữ cảnh kiến trúc, lưu ý đặc biệt từ API bên thứ ba. |
| `HACK:` | Giải pháp tạm thời | Đánh dấu đoạn code chưa tối ưu phải viết do giới hạn bên ngoài. |

### Ví dụ:
```python
# TODO: Implement chunked multipart upload for files larger than 100MB
def upload_video_file(file_path: str) -> str:
    pass

# FIXME: Handle race condition when multiple workers process the same video ID
def acquire_processing_lock(video_id: str) -> bool:
    pass

# NOTE: Third-party payment gateway requires raw payload for signature verification
raw_payload = await request.body()

# HACK: Sleep 50ms before releasing file handle on Windows to avoid access denied error
time.sleep(0.05)
```

---

## 4. Inline Comments (Comment Cùng Dòng Code)

- Hạn chế lạm dụng inline comments.
- Đặt cách câu lệnh ít nhất **2 dấu cách**, bắt đầu bằng `# ` và 1 dấu cách.

```python
# Đúng:
RATE_LIMIT_CEILING = 120  # Requests allowed per minute per IP address

# Tránh (Làm rối các dòng lệnh đơn giản):
user_id = token.sub  # get user id from token
```
