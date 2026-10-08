# Installation & Setup Guide for EngVid Backend

🌐 **Language / Ngôn ngữ:** **English** | [Tiếng Việt](../../vi/setup/installation.md)

---

This guide provides a comprehensive walkthrough for configuring your local development environment and running the **EngVid Backend (`engvid-be`)** service.

---

## 1. Prerequisites

Before getting started, ensure you have the following installed on your machine:

- **Python:** Version `3.14` or higher.
  - Verify your installation:
    - **macOS / Linux:**
      ```bash
      python3 --version
      ```
    - **Windows:**
      ```cmd
      python --version
      # or
      py --version
      ```
- **Git:** Version control tool.

---

## 2. Setting Up the Environment

### Step 1: Clone the Repository (if not already local)
```bash
git clone https://github.com/<your-username>/engvid-be.git
cd engvid-be
```

### Step 2: Create a Virtual Environment
A virtual environment isolates project dependencies from your system-wide packages.

```bash
# Create a virtual environment named .venv
python3 -m venv .venv
```

### Step 3: Activate the Virtual Environment

- **On macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

- **On Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

- **On Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

> [!TIP]
> Once activated, your terminal prompt will be prefixed with `(.venv)`.

---

## 3. Installing Dependencies

Install the required packages using `pip`:

```bash
# Upgrade pip to the latest version
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

---

## 4. Running the Development Server

Run the development server using Python's module launcher to ensure the virtual environment packages are properly used:

```bash
python -m fastapi dev app/main.py
```

Alternatively, you can run directly with `uvicorn`:
```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## 5. Accessing from Other Devices on the Same Network (LAN)

By default, the server listens only on `127.0.0.1` (localhost). To allow other devices (mobile test devices, frontend running on another machine) on the same Wi-Fi/LAN to access your API:

1. **Launch the server with the `--host 0.0.0.0` flag:**
   ```bash
   python -m fastapi dev app/main.py --host 0.0.0.0
   ```

2. **Find your machine's local IP address:**
   - **macOS:** `ipconfig getifaddr en0` (or check *System Settings > Wi-Fi > Details*)
   - **Linux:** `hostname -I`
   - **Windows:** `ipconfig` (look for *IPv4 Address*)

3. **Access from the other device's browser:**
   ```text
   http://<YOUR_LOCAL_IP>:8000/docs
   ```
   *Example: `http://192.168.1.15:8000/docs`*

> [!NOTE]
> If connection is blocked, ensure your operating system's firewall allows incoming connections on port `8000`.

---

## 6. Verifying the API

You can verify that the server is responding by sending a `GET` request:

```bash
curl http://127.0.0.1:8000/
```

**Expected Response:**
```json
{
  "status": "ok",
  "message": "Welcome to EngVid Backend API"
}
```

---

## 7. Troubleshooting Common Issues

### Issue: `command not found: python3`
- Ensure Python is installed and added to your system `PATH`.
- On some systems, use `python` instead of `python3`.

### Issue: Port 8000 is already in use
- Specify a custom port when launching the server:
  ```bash
  fastapi dev app/main.py --port 8080
  ```

### Issue: Permission denied when activating venv on Windows PowerShell
- Open PowerShell as Administrator and run:
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
