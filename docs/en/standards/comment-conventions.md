# Code Comment Conventions for EngVid Backend

🌐 **Language / Ngôn ngữ:** **English** | [Tiếng Việt](../../vi/standards/comment-conventions.md)

---

Clear, purposeful comments make the codebase approachable and prevent regressions. This guide establishes the commenting standards for the `engvid-be` project.

---

## 1. General Principles

### Language
- **All code comments and docstrings must be written in English.**

### Explain "Why", Not "What"
- Good code is mostly self-explanatory through meaningful naming and clean structure.
- Comments should clarify **business intent**, **non-obvious constraints**, **edge cases**, or **workarounds**, not describe obvious Python syntax.

```python
# Bad (States the obvious syntax):
# increment counter by 1
counter += 1

# Good (Explains the underlying reason):
# ffmpeg segment indexing requires 1-based indexing for stream compatibility
counter += 1
```

### Keep Comments Fresh
- An outdated comment is worse than no comment. When updating logic, update or delete the relevant comments immediately.

### No Commented-Out (Dead) Code
- **Never commit commented-out code blocks.**
- Git maintains the full history. If code is no longer needed, delete it completely.

---

## 2. Docstrings Conventions (PEP 257 & Google Style)

Every public module, class, method, and function must include a docstring using triple double-quotes (`"""..."""`). We follow the **Google Python Style** for docstrings.

### Function / Method Docstring Format

```python
def transcode_video(
    source_path: str,
    target_resolution: str,
    bitrate_kbps: int = 1500,
) -> str:
    """Transcodes an input video file to the specified target resolution.

    Executes asynchronous ffmpeg subprocess to re-encode the source video
    while maintaining audio channel fidelity.

    Args:
        source_path: Absolute file system path to the original raw video.
        target_resolution: Video resolution string (e.g., '1080p', '720p').
        bitrate_kbps: Video bitrate limit in kilobits per second. Defaults to 1500.

    Returns:
        The absolute file path of the successfully transcoded video file.

    Raises:
        FileNotFoundError: If `source_path` does not exist on disk.
        TranscodingError: If ffmpeg fails during stream conversion.
    """
    # Function implementation...
```

### Class Docstring Format

```python
class StorageService:
    """Manages file persistence to local disk and S3-compatible cloud storage.

    Attributes:
        bucket_name: Cloud bucket name for public asset distribution.
        cache_dir: Local temporary scratch directory for in-flight uploads.
    """

    def __init__(self, bucket_name: str, cache_dir: str) -> None:
        self.bucket_name = bucket_name
        self.cache_dir = cache_dir
```

---

## 3. Action Comments & Annotation Tags

When leaving notes in the codebase, use standardized uppercase tags:

| Tag | Meaning | Usage |
| :--- | :--- | :--- |
| `TODO:` | Planned work | Indicates a feature or optimization planned for a future task. |
| `FIXME:` | Known defect | Highlights a known issue or bug that needs immediate resolution. |
| `NOTE:` | Important context | Explains architectural choices, tricky behavior, or external dependency caveats. |
| `HACK:` | Workaround | Indicates temporary or unconventional code implemented due to a bug or limitation elsewhere. |

### Examples:
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

## 4. Inline Comments

- Use inline comments sparingly.
- Place them on the same line as the statement, separated by at least **two spaces**, starting with `# ` and a single space.

```python
# Correct:
RATE_LIMIT_CEILING = 120  # Requests allowed per minute per IP address

# Avoid (Clutters simple statements):
user_id = token.sub  # get user id from token
```
