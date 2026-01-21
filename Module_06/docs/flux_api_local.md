# Flux.2 BFL-Compatible API Documentation

## 🚀 Overview
High-performance backend for local image generation using **Flux.2 [klein]** models, fully compatible with the Black Forest Labs (BFL) API specification.

## 🔒 Authentication
All requests to generation endpoints require the `x-key` header.

**API Key:**
check TG chat

## 📍 Base URLs
- **Public API:** `http://api.qix.ee`
- **Internal:** `http://192.168.1.12:8000`

---

## 🛰️ Endpoints

### 1. Trigger Generation
`POST /v1/{model_type}`
- **Models:** `flux-2-klein-4b`, `flux-2-klein-9b`
- **Headers:** `x-key: your_api_key`
- **Body (JSON):**
```json
{
  "prompt": "A futuristic city at sunset, cinematic lighting",
  "aspect_ratio": "1:1",
  "steps": 4,
  "seed": 42
}
```
- **Response:**
```json
{
  "id": "20260121_115610_abcd1234",
  "status": "Task_Queued",
  "polling_url": "http://api.qix.ee/v1/get_result?id=20260121_115610_abcd1234"
}
```

### 2. Get Result (Polling)
`GET /v1/get_result?id={task_id}`
- **Headers:** `x-key` (not strictly required but recommended)
- **Response (Processing):**
```json
{
  "id": "20260121_115610_abcd1234",
  "status": "Processing"
}
```
- **Response (Ready):**
```json
{
  "id": "20260121_115610_abcd1234",
  "status": "Ready",
  "result": {
    "sample": "http://api.qix.ee/outputs/flux_20260121_115610_abcd1234.png"
  }
}
```

### 3. History (Gallery)
`GET /history`
- **Description:** Returns a list of all successful generations with metadata.
- **Query Params:**
    - `limit` (int, default: 50)
    - `offset` (int, default: 0)
    - `query` (string, optional): Search by prompt keyword.
- **Response Example:**
```json
[
  {
    "id": "20260121_115610_abcd1234",
    "prompt": "...",
    "model": "flux-2-klein-4b",
    "status": "Ready",
    "result_url": "http://api.qix.ee/outputs/flux_20260121_115610_abcd1234.png",
    "url": "http://api.qix.ee/outputs/flux_20260121_115610_abcd1234.png",
    "metadata": "{\"aspect_ratio\": \"1:1\", \"steps\": 4, \"seed\": 42}",
    "created_at": "2026-01-21T11:56:10"
  }
]
```

---

## 🖼️ Static Assets
Images are served directly via the `/outputs/` prefix:
- `http://api.qix.ee/outputs/{filename}`

---

## 🛠️ Implementation Details
1. **Asynchronous Queue:** Requests are instantly queued in a SQLite database. A dedicated GPU worker pulls tasks sequentially.
2. **Dynamic URLs:** The `BASE_URL` from `config.py` is used to generate absolute URLs in the history and polling responses.
3. **Model Switching:** The worker automatically loads the requested model (4b/9b) on demand, clearing VRAM as needed.
