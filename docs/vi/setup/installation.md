# Hướng Dẫn Cài Đặt & Chạy Dự Án EngVid Backend

🌐 **Language / Ngôn ngữ:** [English](../../en/setup/installation.md) | **Tiếng Việt**

---

Tài liệu này hướng dẫn chi tiết từng bước thiết lập môi trường phát triển cục bộ và khởi chạy dịch vụ **EngVid Backend (`engvid-be`)**.

---

## 1. Yêu Cầu Cài Đặt Ban Đầu

Trước khi bắt đầu, hãy đảm bảo máy tính của bạn đã cài đặt các công cụ sau:

- **Python:** Phiên bản `3.14` trở lên.
  - Kiểm tra phiên bản hiện tại:
    - **Trên macOS / Linux:**
      ```bash
      python3 --version
      ```
    - **Trên Windows:**
      ```cmd
      python --version
      # hoặc
      py --version
      ```
- **Git:** Công cụ quản lý mã nguồn.

---

## 2. Thiết Lập Môi Trường Ảo (Virtual Environment)

### Bước 1: Di chuyển vào thư mục dự án
```bash
cd engvid-be
```

### Bước 2: Tạo môi trường ảo
Môi trường ảo giúp cô lập các thư viện của dự án, tránh xung đột với các thư viện chung của hệ điều hành.

```bash
# Tạo môi trường ảo có tên là .venv
python3 -m venv .venv
```

### Bước 3: Kích hoạt môi trường ảo

- **Trên macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

- **Trên Windows (Command Prompt - CMD):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

- **Trên Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

> [!TIP]
> Sau khi kích hoạt thành công, bạn sẽ thấy tiền tố `(.venv)` xuất hiện ở đầu dòng lệnh terminal.

---

## 3. Cài Đặt Các Thư Viện Phụ Thuộc (Dependencies)

Sử dụng `pip` để cài đặt các gói cần thiết:

```bash
# Cập nhật pip lên bản mới nhất
pip install --upgrade pip

# Cài đặt toàn bộ thư viện từ file requirements.txt
pip install -r requirements.txt
```

---

## 4. Khởi Chạy Server Phát Triển

Chạy server thông qua trình gọi module của Python (`python -m`) để đảm bảo các gói thư viện trong môi trường ảo được sử dụng chính xác:

```bash
python -m fastapi dev app/main.py
```

Hoặc khởi chạy trực tiếp thông qua `uvicorn`:
```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## 5. Truy Cập Từ Thiết Bị Khác Trong Cùng Mạng (LAN)

Mặc định, server chỉ lắng nghe trên `127.0.0.1` (chỉ máy cục bộ truy cập được). Để các thiết bị khác (điện thoại test, máy tính chạy frontend của đồng nghiệp) trong cùng mạng Wi-Fi/LAN có thể gọi API:

1. **Khởi chạy server với cờ `--host 0.0.0.0`:**
   ```bash
   python -m fastapi dev app/main.py --host 0.0.0.0
   ```

2. **Lấy địa chỉ IP nội bộ của máy bạn:**
   - **macOS:** `ipconfig getifaddr en0` (hoặc vào *Cài đặt hệ thống > Wi-Fi > Chi tiết*)
   - **Linux:** `hostname -I`
   - **Windows:** `ipconfig` (tìm dòng *IPv4 Address*)

3. **Truy cập từ trình duyệt trên thiết bị khác:**
   ```text
   http://<IP_NOI_BO_CUA_BAN>:8000/docs
   ```
   *Ví dụ: `http://192.168.1.15:8000/docs`*

> [!NOTE]
> Nếu thiết bị khác không kết nối được, hãy kiểm tra xem Tường lửa (Firewall) trên máy tính của bạn có đang chặn cổng `8000` hay không.

---

## 6. Kiểm Tra Kết Nối API

Bạn có thể kiểm tra xem API đã hoạt động bình thường chưa bằng lệnh `curl`:

```bash
curl http://127.0.0.1:8000/
```

**Kết quả phản hồi mong đợi:**
```json
{
  "status": "ok",
  "message": "Welcome to EngVid Backend API"
}
```

---

## 7. Xử Lý Các Lỗi Thường Gặp (Troubleshooting)

### Lỗi: `command not found: python3`
- Đảm bảo Python đã được cài đặt và thêm vào biến môi trường `PATH`.
- Trên một số hệ điều hành (như Windows), hãy thử gõ `python` thay vì `python3`.

### Lỗi: Cổng 8000 đã bị ứng dụng khác chiếm dụng (Port already in use)
- Khởi chạy server trên cổng khác (ví dụ cổng 8080):
  ```bash
  fastapi dev app/main.py --port 8080
  ```

### Lỗi: Không kích hoạt được venv trên Windows PowerShell (`Script Execution Disabled`)
- Mở PowerShell dưới quyền Administrator và chạy lệnh cấp quyền:
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
