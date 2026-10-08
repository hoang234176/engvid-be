# EngVid Backend (`engvid-be`)

Backend API services for the **EngVid** (English Video Learning) platform, built with **Python 3.14+** and **FastAPI**.

---

## ⚡ Tech Stack & Requirements

- **Runtime:** Python `>= 3.14`
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Standard edition with Uvicorn ASGI server)
- **Dependency Management:** `requirements.txt`
- **Standards:** Strict PEP 8, Type Hinting, and RESTful API standards

---

## 🚀 Quick Start

Get the local development server up and running in under a minute:

```bash
# 1. Clone the repository
git clone https://github.com/hoang234176/engvid-be.git
cd engvid-be

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate.bat    # Windows (CMD)
# .venv\Scripts\Activate.ps1    # Windows (PowerShell)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the development server
python -m fastapi dev app/main.py

# Optional: To allow other devices on the same Wi-Fi/LAN to access:
# python -m fastapi dev app/main.py --host 0.0.0.0
```

The service will be live at:
- **API Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

> 💡 **Tip:** To test from a mobile phone or another machine on your local Wi-Fi, run with `--host 0.0.0.0` and open `http://<YOUR_LOCAL_IP>:8000/docs`. See the [Installation Guide](docs/en/setup/installation.md#5-accessing-from-other-devices-on-the-same-network-lan) for details.

> 📖 **Need a step-by-step setup guide or troubleshooting help?**  
> Check out the [Detailed Installation Guide (EN)](docs/en/setup/installation.md) | [Hướng Dẫn Cài Đặt Chi Tiết (VI)](docs/vi/setup/installation.md).

---

## 📂 Project Structure

```text
engvid-be/
├── .gitignore                      # Git ignored files & environments
├── CONTRIBUTING.md                 # Contribution guidelines (English)
├── CONTRIBUTING.vi.md              # Quy tắc đóng góp (Tiếng Việt)
├── README.md                       # Project overview & documentation index
├── requirements.txt                # Python dependencies
├── app/                            # Application source code
│   ├── __init__.py
│   └── main.py                     # FastAPI application entrypoint
└── docs/                           # Project documentation
    ├── en/                         # English documentation
    │   ├── setup/
    │   │   └── installation.md     # Installation & runtime guide
    │   └── standards/
    │       ├── pep8-guide.md       # PEP 8 style guide
    │       ├── type-hinting-guide.md # Modern Python type hints
    │       ├── comment-conventions.md# Comments & docstrings standards
    │       └── http-status-codes.md  # HTTP status & streaming standards
    └── vi/                         # Vietnamese documentation
        ├── setup/
        │   └── installation.md     # Hướng dẫn cài đặt chi tiết
        └── standards/
            ├── pep8-guide.md       # Quy chuẩn phong cách PEP 8
            ├── type-hinting-guide.md # Quy chuẩn Type Hinting
            ├── comment-conventions.md# Quy ước comment code
            └── http-status-codes.md  # Quy chuẩn mã HTTP & streaming
```

---

## 📚 Documentation Index

We maintain comprehensive documentation in both **English** and **Tiếng Việt**:

| Topic | English (EN) | Tiếng Việt (VI) |
| :--- | :--- | :--- |
| **Contributing Rules & Git Workflow** | [CONTRIBUTING.md](CONTRIBUTING.md) | [CONTRIBUTING.vi.md](CONTRIBUTING.vi.md) |
| **Setup & Installation** | [Installation Guide](docs/en/setup/installation.md) | [Hướng Dẫn Cài Đặt](docs/vi/setup/installation.md) |
| **PEP 8 Code Style** | [PEP 8 Guide](docs/en/standards/pep8-guide.md) | [Quy Chuẩn PEP 8](docs/vi/standards/pep8-guide.md) |
| **Type Hinting Standards** | [Type Hinting Guide](docs/en/standards/type-hinting-guide.md) | [Hướng Dẫn Type Hinting](docs/vi/standards/type-hinting-guide.md) |
| **Code Comment Conventions** | [Comment Conventions](docs/en/standards/comment-conventions.md) | [Quy Ước Viết Comment](docs/vi/standards/comment-conventions.md) |
| **HTTP Status Codes & Streaming** | [HTTP Status Codes](docs/en/standards/http-status-codes.md) | [Quy Chuẩn Mã HTTP](docs/vi/standards/http-status-codes.md) |

---

## 🛡️ Git Workflow Rules

- **Branch Protection:** Direct commits to `main` are strictly forbidden.
- **Branch Naming:** Follow the 3-tier hierarchy: `<type>/<main-feature>/<sub-feature>` (e.g., `feat/video-processing/hls-transcoding`).
- **Commits:** Conventional Commits in **English** only.
- **Pull Requests:** Must be reviewed and approved on GitHub before merging into `main`.