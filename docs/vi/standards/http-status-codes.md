# Quy Chuẩn Mã Phản Hồi HTTP Cho EngVid Backend

🌐 **Language / Ngôn ngữ:** [English](../../en/standards/http-status-codes.md) | **Tiếng Việt**

---

Tài liệu này quy định các **Mã trạng thái HTTP (HTTP Status Codes)** và **Cấu trúc phản hồi dữ liệu (Response Format)** được sử dụng thống nhất trên toàn bộ hệ thống API của `engvid-be`. Việc chuẩn hóa này giúp việc giao tiếp giữa Backend và các ứng dụng Client (Web, Mobile App, Trình phát Video) luôn chính xác và nhất quán.

---

## 1. Phát Trực Tuyến Video & Phân Phối Đa Phương Tiện (Đặc Thù EngVid)

Vì `engvid-be` là nền tảng học tiếng Anh qua video, các mã phục vụ truyền phát trực tuyến (streaming) đóng vai trò cốt lõi:

| Mã | Trạng thái | Mục đích sử dụng trong EngVid |
| :--- | :--- | :--- |
| **`200`** | **OK** | Tải toàn bộ file hoặc lấy dữ liệu thông tin bài học (metadata của bài học, danh sách khóa học). |
| **`206`** | **Partial Content** | **Phát trực tuyến video/audio theo đoạn byte (Byte-range streaming).** Trả về khi trình phát video yêu cầu một đoạn cụ thể thông qua header `Range` (ví dụ: người dùng tua video tới phút thứ 10). |
| **`416`** | **Range Not Satisfiable** | Vị trí byte yêu cầu vượt quá kích thước thực tế của file video (ví dụ: file chỉ nặng 200MB nhưng yêu cầu tua ở byte thứ 300MB). |

### Ví Dụ Header Cho Mã 206 Streaming:
- **Request từ trình duyệt:** `Range: bytes=0-1048575` (xin 1MB đầu tiên)
- **Status trả về:** `206 Partial Content`
- **Response Headers từ server:**
  ```http
  Content-Range: bytes 0-1048575/52428800
  Content-Length: 1048576
  Content-Type: video/mp4
  ```

---

## 2. Tác Vụ Xử Lý Chạy Ngầm (Video Processing Jobs)

Các tác vụ tốn nhiều thời gian (chuyển mã video đa độ phân giải, trích xuất âm thanh, AI tạo phụ đề tự động) không được làm nghẽn kết nối HTTP:

| Mã | Trạng thái | Mục đích sử dụng trong EngVid |
| :--- | :--- | :--- |
| **`202`** | **Accepted** | Yêu cầu đã được tiếp nhận và đưa vào hàng đợi xử lý ngầm (ví dụ: đã nhận video tải lên, đưa vào hàng đợi transcode hoặc AI bóc băng). Server trả về ngay mã công việc (task ID) để client theo dõi tiến độ. |

---

## 3. Các Mã Chuẩn Cho Thao Tác Dữ Liệu (RESTful CRUD)

| Mã | Trạng thái | Phương thức | Mục đích sử dụng trong EngVid |
| :--- | :--- | :--- | :--- |
| **`200`** | **OK** | `GET`, `PUT`, `PATCH` | Lấy dữ liệu hoặc cập nhật bài học/thông tin thành công. |
| **`201`** | **Created** | `POST` | Tạo mới tài nguyên thành công (ví dụ: tạo bài học mới, đăng ký tài khoản, gửi bình luận). |
| **`204`** | **No Content** | `DELETE` | Thao tác thành công nhưng không cần trả dữ liệu body (ví dụ: xóa video, bỏ lưu bài học yêu thích). |

---

## 4. Lỗi Phía Người Dùng Gửi Lên (Client Errors - 4xx)

| Mã | Trạng thái | Mục đích sử dụng trong EngVid |
| :--- | :--- | :--- |
| **`400`** | **Bad Request** | Cú pháp request không hợp lệ hoặc thiếu các tham số cơ bản. |
| **`401`** | **Unauthorized** | Chưa đăng nhập, thiếu token xác thực (JWT) hoặc token đã hết hạn. |
| **`403`** | **Forbidden** | Đã đăng nhập nhưng không có quyền (ví dụ: học viên gói miễn phí cố xem video dành riêng cho gói VIP, hoặc sửa video của quản trị viên). |
| **`404`** | **Not Found** | Không tìm thấy tài nguyên (ví dụ: ID bài học hoặc ID video không tồn tại). |
| **`409`** | **Conflict** | Xung đột dữ liệu hệ thống (ví dụ: email đăng ký đã tồn tại, slug của bài học bị trùng). |
| **`413`** | **Content Too Large** | File video hoặc tệp đính kèm tải lên vượt quá dung lượng tối đa cho phép. |
| **`422`** | **Unprocessable Entity** | Dữ liệu đúng cấu trúc JSON nhưng vi phạm quy tắc ràng buộc (Mặc định do FastAPI/Pydantic trả về khi dữ liệu đầu vào không hợp lệ). |
| **`429`** | **Too Many Requests** | Gửi quá nhiều request trong thời gian ngắn (vượt giới hạn Rate Limit). |

---

## 5. Lỗi Phía Hệ Thống Máy Chủ (Server Errors - 5xx)

| Mã | Trạng thái | Mục đích sử dụng trong EngVid |
| :--- | :--- | :--- |
| **`500`** | **Internal Server Error** | Lỗi sập hệ thống hoặc lỗi code chưa được bắt (unhandled exception). |
| **`502`** | **Bad Gateway** | Lỗi khi backend kết nối đến dịch vụ bên ngoài (ví dụ: dịch vụ AI phiên âm, Cloudflare, AWS S3). |
| **`503`** | **Service Unavailable** | Máy chủ đang bảo trì định kỳ hoặc bị quá tải lưu lượng đột biến. |
| **`504`** | **Gateway Timeout** | Quá thời gian chờ phản hồi từ tiến trình xử lý khác (ví dụ: worker xử lý ffmpeg bị timeout). |

---

## 6. Cấu Trúc JSON Trả Về Chuẩn Khi Xảy Ra Lỗi

Tất cả các phản hồi lỗi (`4xx` và `5xx`) bắt buộc phải tuân theo cấu trúc JSON đồng nhất:

```json
{
  "error": {
    "code": "LESSON_NOT_FOUND",
    "message": "Không tìm thấy bài học video với mã 'les_123'.",
    "details": null
  }
}
```

Đối với lỗi kiểm tra dữ liệu đầu vào (`422 Unprocessable Entity`), trường `details` sẽ chứa chi tiết từng trường bị lỗi:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu gửi lên không đúng định dạng yêu cầu.",
    "details": [
      {
        "field": "title",
        "issue": "Tiêu đề bài học phải có ít nhất 3 ký tự"
      }
    ]
  }
}
```
