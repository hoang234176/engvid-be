# Contributing Guidelines for EngVid Backend

🌐 **Language / Ngôn ngữ:** **English** | [Tiếng Việt](CONTRIBUTING.vi.md)

---

Thank you for your interest in contributing to **EngVid Backend (`engvid-be`)**! To maintain code quality, consistency, and a smooth development workflow, please read and follow these guidelines.

---

## 1. Project Prerequisites

- **Language:** Python `>= 3.14`
- **Environment:** Use a dedicated virtual environment (`venv` or `poetry`).
- **Operating Standards:**
  - Code style must comply with [PEP 8 Style Guide](docs/en/standards/pep8-guide.md).
  - All production code requires [Python Type Hinting](docs/en/standards/type-hinting-guide.md).
  - Code comments and docstrings must follow [Comment Conventions](docs/en/standards/comment-conventions.md).

---

## 2. Git Branching Strategy

We follow a Gitflow-inspired branching workflow:
- **`main`**: Production-ready branch. Only fully tested, completed releases are merged here from `develop`.
- **`develop`**: Primary development and integration branch. All feature and fix branches branch off from `develop` and merge back into `develop`.

> [!CAUTION]
> **Direct commits to `main` and `develop` are strictly forbidden!**
> All changes must be submitted via a Pull Request (PR) on GitHub targeting `develop`, requiring review and approval from the project owner before merging. Direct pushes to `main` are reserved exclusively for validated release milestones.

### Branch Naming Format
Branch names must use lowercase **`kebab-case`** and follow a **3-tier hierarchy**:

```text
<type>/<main-feature>/<sub-feature>
```

- `<type>`: `feat`, `fix`, `refactor`, `perf`, `docs`, `chore`
- `<main-feature>`: High-level domain or module (e.g., `auth`, `video-processing`, `user-management`, `billing`)
- `<sub-feature>`: Specific scope or task (e.g., `google-oauth`, `hls-transcoding`, `password-reset`)

### Examples:
- `feat/video-processing/hls-transcoding`
- `feat/auth/google-oauth`
- `fix/payment-gateway/stripe-webhook-timeout`
- `refactor/database/optimize-video-queries`

---

## 3. Commit Message Conventions

All commit messages **must be written in English** following the [Conventional Commits](https://www.conventionalcommits.org/) format.

### Commit Format

#### Single-line Commit:
```text
<type>(<scope>): <summary in English>
```

#### Detailed / Multi-line Commit:
```text
<type>(<scope>): <short summary in English>

- <detailed change description 1>
- <detailed change description 2>
- <detailed change description 3>
```

### Commit Types

| Type | Description |
| :--- | :--- |
| **`feat`** | A new feature or capability |
| **`fix`** | A bug fix |
| **`docs`** | Documentation changes only |
| **`style`** | Code style/formatting changes with no logical impact |
| **`refactor`** | Code refactoring without fixing bugs or adding features |
| **`perf`** | Performance improvement |
| **`test`** | Adding or correcting automated tests |
| **`build`** | Build system, packaging, or dependency updates |
| **`ci`** | CI/CD pipeline or configuration updates |
| **`chore`** | Maintenance tasks, tooling, or repository housekeeping |
| **`revert`** | Reverting a previous commit |

### Commit Examples

**Single-line:**
```bash
git commit -m "feat(auth): implement jwt token refreshment"
git commit -m "fix(video-upload): handle file size limit exception properly"
```

**Multi-line with bullet points:**
```bash
git commit -m "feat(video-processing): add hls transcoding pipeline

- add ffmpeg subprocess wrapper for segment creation
- generate master playlist file and resolution variants
- upload chunks to s3 bucket asynchronously"
```

---

## 4. Coding Standards & Conventions

Before submitting code, ensure it aligns with our documentation standards:

1. **[PEP 8 Style Guide](docs/en/standards/pep8-guide.md)**
   - 4-space indentation, no tabs.
   - Max line length 88-100 characters.
   - `snake_case` for functions/variables, `PascalCase` for classes.
2. **[Python Type Hinting Guide](docs/en/standards/type-hinting-guide.md)**
   - Mandatory parameter and return type hints for all functions/methods.
   - Use built-in generics (`list[str]`, `dict[str, Any]`, `X | None`).
3. **[Code Comment Conventions](docs/en/standards/comment-conventions.md)**
   - 100% written in English.
   - Explain "Why", not "What".
   - Google-style docstrings for public classes and functions.
   - No commented-out dead code.
4. **[HTTP Status Codes & API Standards](docs/en/standards/http-status-codes.md)**
   - Proper use of streaming codes (`206 Partial Content`, `416`).
   - Asynchronous job handling (`202 Accepted`).
   - Standardized JSON error response format.

---

## 5. Pull Request (PR) Workflow

1. **Update `develop`:** Pull the latest changes from upstream `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   ```
2. **Create Branch:** Create a branch off `develop` following the 3-tier naming convention:
   ```bash
   git checkout -b feat/video-processing/hls-transcoding
   ```
3. **Implement & Test:** Write clean, typed, and well-commented code.
4. **Format & Verify:**
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
6. **Open PR:** Submit a Pull Request into **`develop`** with a clear description and testing checklist.
