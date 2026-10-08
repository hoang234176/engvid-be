# HTTP Status Codes & API Response Standards for EngVid Backend

🌐 **Language / Ngôn ngữ:** **English** | [Tiếng Việt](../../vi/standards/http-status-codes.md)

---

This document outlines the standard **HTTP Status Codes** and **Response Formats** used across the `engvid-be` API services. Consistent status codes ensure reliable communication between the backend and client applications (Web, Mobile, Video Player).

---

## 1. Video Streaming & Media Delivery (Crucial for EngVid)

Because `engvid-be` powers an English Video Learning platform, streaming and media delivery have dedicated status codes:

| Code | Status | Usage in EngVid |
| :--- | :--- | :--- |
| **`200`** | **OK** | Full file delivery or metadata retrieval (e.g., fetching video lesson metadata, course details). |
| **`206`** | **Partial Content** | **Byte-range video/audio streaming.** Returned when the video player requests a specific segment of a lesson via the `Range` header (e.g., seeking to a timestamp). |
| **`416`** | **Range Not Satisfiable** | The requested byte range is beyond the video file bounds (e.g., requested bytes 500MB+ when the file is only 200MB). |

### Example 206 Streaming Headers:
- **Request:** `Range: bytes=0-1048575`
- **Response Status:** `206 Partial Content`
- **Response Headers:**
  ```http
  Content-Range: bytes 0-1048575/52428800
  Content-Length: 1048576
  Content-Type: video/mp4
  ```

---

## 2. Asynchronous Jobs & Video Processing

Long-running operations (transcoding, AI subtitle generation, audio extraction) must not block HTTP requests:

| Code | Status | Usage in EngVid |
| :--- | :--- | :--- |
| **`202`** | **Accepted** | Request accepted and queued for background processing (e.g., video upload received, queued for transcoding or AI transcription). Returns a task ID. |

---

## 3. Standard RESTful CRUD Codes

| Code | Status | Method | Usage in EngVid |
| :--- | :--- | :--- | :--- |
| **`200`** | **OK** | `GET`, `PUT`, `PATCH` | Resource successfully retrieved or updated. |
| **`201`** | **Created** | `POST` | New resource created (e.g., new lesson created, user registered, comment posted). |
| **`204`** | **No Content** | `DELETE` | Action succeeded, no response body returned (e.g., deleted bookmark, removed video). |

---

## 4. Client Errors (4xx)

| Code | Status | Usage in EngVid |
| :--- | :--- | :--- |
| **`400`** | **Bad Request** | Malformed request syntax or unprocessable parameters. |
| **`401`** | **Unauthorized** | Missing, invalid, or expired authentication token (JWT). |
| **`403`** | **Forbidden** | User is authenticated but lacks required permission (e.g., free student attempting to access premium lessons or modify admin videos). |
| **`404`** | **Not Found** | Resource does not exist (e.g., lesson ID not found). |
| **`409`** | **Conflict** | Resource state conflict (e.g., email already registered, lesson slug already exists). |
| **`413`** | **Content Too Large** | Uploaded video or attachment exceeds maximum allowed file size. |
| **`422`** | **Unprocessable Entity** | Schema or data validation error (FastAPI/Pydantic default when request fields are invalid). |
| **`429`** | **Too Many Requests** | Rate limit exceeded (e.g., too many login attempts or excessive API calls). |

---

## 5. Server Errors (5xx)

| Code | Status | Usage in EngVid |
| :--- | :--- | :--- |
| **`500`** | **Internal Server Error** | Unexpected server crash or unhandled runtime exception. |
| **`502`** | **Bad Gateway** | Failure communicating with an upstream service (e.g., AI transcribing service, Cloudflare, S3). |
| **`503`** | **Service Unavailable** | Server temporarily unavailable due to maintenance or extreme traffic overload. |
| **`504`** | **Gateway Timeout** | Upstream operation timed out (e.g., ffmpeg worker timeout). |

---

## 6. Standardized Error Response Format

All error responses (`4xx` and `5xx`) must follow a unified JSON payload structure:

```json
{
  "error": {
    "code": "LESSON_NOT_FOUND",
    "message": "The requested video lesson with ID 'les_123' was not found.",
    "details": null
  }
}
```

For validation errors (`422 Unprocessable Entity`), `details` provides field-specific messages:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request payload validation failed.",
    "details": [
      {
        "field": "title",
        "issue": "String should have at least 3 characters"
      }
    ]
  }
}
```
