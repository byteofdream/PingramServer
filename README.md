# Pingram Server

Python FastAPI backend for Pingram messenger.

## Requirements

- Python 3.11+
- `pip`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run (development)

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## Health Check

```bash
curl http://127.0.0.1:8000/health
```

## Auth API

### Register

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"phone":"+380991234567","password":"password123","username":"new_user"}'
```

### Login

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"phone":"+380501112233","password":"password123"}'
```
