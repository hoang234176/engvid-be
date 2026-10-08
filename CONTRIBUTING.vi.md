# Hướng Dẫn Đóng Góp Dự Án EngVid Backend

🌐 **Language / Ngôn ngữ:** [English](CONTRIBUTING.md) | **Tiếng Việt**

---

Cảm ơn bạn đã quan tâm và tham gia đóng góp cho dự án **EngVid Backend (`engvid-be`)**! Nhằm đảm bảo chất lượng mã nguồn, tính nhất quán và quy trình làm việc hiệu quả, vui lòng đọc và tuân thủ các quy tắc dưới đây.

---

## 1. Yêu Cầu Tiên Quyết (Prerequisites)

- **Ngôn ngữ:** Python `>= 3.14`
- **Môi trường ảo:** Luôn chạy trên môi trường ảo riêng biệt (`venv` hoặc `poetry`).
- **Quy chuẩn bắt buộc:**
  - Định dạng code tuân thủ theo [Quy Chuẩn PEP 8](docs/vi/standards/pep8-guide.md).
  - Bắt buộc khai báo [Type Hinting](docs/vi/standards/type-hinting-guide.md) cho toàn bộ code.
  - Viết comment và docstrings theo [Quy Ước Comment Code](docs/vi/standards/comment-conventions.md).

---

## 2. Chiến Lược Phân Nhánh Git (Branching Strategy)

Dự án áp dụng mô hình phân nhánh theo luồng Gitflow:
- **`main`**: Nhánh production ổn định. Chỉ gộp các bản phát hành (release) đã hoàn thiện và kiểm thử kỹ lưỡng từ `develop`.
- **`develop`**: Nhánh tích hợp và phát triển chính. Tất cả nhánh tính năng (`feat`) và sửa lỗi (`fix`) đều tách ra từ `develop` và tạo PR gộp về `develop`.

> [!CAUTION]
> **Tuyệt đối nghiêm cấm commit trực tiếp vào cả hai nhánh `main` và `develop`!**
> Mọi thay đổi bắt buộc phải được tạo qua Pull Request (PR) trên GitHub hướng vào nhánh **`develop`**, đồng thời phải được chủ dự án phê duyệt (review & approve) mới được phép gộp (merge). Nhánh `main` chỉ nhận code khi hoàn tất một mốc phát hành (release).

### Định Dạng Đặt Tên Nhánh
Tên nhánh sử dụng chữ thường định dạng **`kebab-case`** và tuân theo **cấu trúc 3 cấp**:

```text
<loại>/<tên-chức-năng-chính>/<chức-năng-phát-triển>
```

- `<loại>`: `feat`, `fix`, `refactor`, `perf`, `docs`, `chore`
- `<tên-chức-năng-chính>`: Module hoặc phân hệ lớn (ví dụ: `auth`, `video-processing`, `user-management`, `billing`)
- `<chức-năng-phát-triển>`: Tên tính năng cụ thể hoặc mã task (ví dụ: `google-oauth`, `hls-transcoding`, `password-reset`)

### Ví dụ:
- `feat/video-processing/hls-transcoding`
- `feat/auth/google-oauth`
- `fix/payment-gateway/stripe-webhook-timeout`
- `refactor/database/optimize-video-queries`

---

## 3. Quy Ước Viết Commit (Commit Messages)

Toàn bộ commit message **bắt buộc phải viết bằng Tiếng Anh** theo chuẩn [Conventional Commits](https://www.conventionalcommits.org/).

### Cấu Trúc Commit

#### Trường hợp commit ngắn gọn (1 dòng):
```text
<tên loại>(<phạm vi>): <mô tả ngắn gọn bằng tiếng Anh>
```

#### Trường hợp liệt kê nhiều thay đổi (nhiều dòng):
```text
<tên loại>(<phạm vi>): <tóm tắt ngắn gọn thay đổi chính bằng tiếng Anh>

- <chi tiết thay đổi 1>
- <chi tiết thay đổi 2>
- <chi tiết thay đổi 3>
```

### Danh Sách Các Loại Commit (Commit Types)

| Loại | Ý nghĩa |
| :--- | :--- |
| **`feat`** | Thêm tính năng mới |
| **`fix`** | Sửa lỗi (bug fix) |
| **`docs`** | Chỉ thay đổi tài liệu |
| **`style`** | Định dạng code, dấu chấm phẩy, không ảnh hưởng logic |
| **`refactor`** | Tái cấu trúc code (không sửa lỗi, không thêm tính năng) |
| **`perf`** | Tối ưu hóa hiệu năng |
| **`test`** | Thêm mới hoặc sửa các bài kiểm thử |
| **`build`** | Thay đổi hệ thống build hoặc cập nhật dependencies |
| **`ci`** | Cập nhật luồng CI/CD |
| **`chore`** | Các công việc bảo trì, cấu hình công cụ linh tinh |
| **`revert`** | Hoàn tác (revert) một commit trước đó |

### Ví Dụ Commit Thực Tế

**Commit 1 dòng:**
```bash
git commit -m "feat(auth): implement jwt token refreshment"
git commit -m "fix(video-upload): handle file size limit exception properly"
```

**Commit nhiều dòng liệt kê chi tiết:**
```bash
git commit -m "feat(video-processing): add hls transcoding pipeline

- add ffmpeg subprocess wrapper for segment creation
- generate master playlist file and resolution variants
- upload chunks to s3 bucket asynchronously"
```

---

## 4. Tiêu Chuẩn Viết Code & Tài Liệu Liên Kết

Trước khi gửi mã nguồn lên kho lưu trữ, hãy đảm bảo tuân thủ các tài liệu quy chuẩn sau:

1. **[Quy Chuẩn Phong Cách Code PEP 8](docs/vi/standards/pep8-guide.md)**
   - Thụt lề 4 dấu cách, không dùng Tab.
   - Giới hạn dòng code từ 88-100 ký tự.
   - `snake_case` cho hàm/biến, `PascalCase` cho class.
2. **[Hướng Dẫn Python Type Hinting](docs/vi/standards/type-hinting-guide.md)**
   - Bắt buộc khai báo kiểu dữ liệu cho tham số và giá trị trả về của mọi hàm.
   - Dùng cú pháp hiện đại (`list[str]`, `dict[str, Any]`, `X | None`).
3. **[Quy Ước Viết Comment Code](docs/vi/standards/comment-conventions.md)**
   - 100% comment viết bằng Tiếng Anh.
   - Giải thích "Tại sao" (Why), không nhắc lại cú pháp "Cái gì" (What).
   - Viết Docstring chuẩn Google Style cho các hàm và class public.
   - Nghiêm cấm commit dead code (code bị comment lại).
4. **[Quy Chuẩn Mã Phản Hồi HTTP & API](docs/vi/standards/http-status-codes.md)**
   - Sử dụng chuẩn xác mã truyền phát video (`206 Partial Content`, `416`).
   - Xử lý tác vụ ngầm chạy lâu (`202 Accepted`).
   - Định dạng JSON trả về lỗi chuẩn hóa.

---

## 5. Quy Trình Tạo Pull Request (PR Workflow)

1. **Đồng bộ `develop` mới nhất:**
   ```bash
   git checkout develop
   git pull origin develop
   ```
2. **Tạo nhánh làm việc:** Tách nhánh từ `develop` và đặt tên đúng chuẩn 3 cấp:
   ```bash
   git checkout -b feat/video-processing/hls-transcoding
   ```
3. **Viết code & kiểm thử:** Đảm bảo code sạch, có type hints và comment đầy đủ.
4. **Kiểm tra linter & type check tự động:**
   ```bash
   ruff format .
   ruff check . --fix
   mypy .
   ```
5. **Commit & Push:**
   ```bash
   git commit -m "feat(video-processing): add hls transcoding pipeline"
   git push origin feat/video-processing/hls-transcoding
   ```
6. **Mở PR:** Gửi Pull Request vào nhánh **`develop`**, kèm mô tả tóm tắt những việc đã làm.
