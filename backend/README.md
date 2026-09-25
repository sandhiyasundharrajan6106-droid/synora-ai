# Synora AI Backend

FastAPI backend for the Synora AI prototype.

## Features

- profile intake
- symptom collection
- eye tracking feature capture
- cognitive test scoring
- feature extraction
- prototype ML screening
- SQLite storage and report generation

## Start locally

```bash
cd "C:\sandhiya project\NeuroGuardAI\backend"
python -m venv .venv
.\.venv\Scripts\python.exe -m ensurepip --upgrade
.\.venv\Scripts\python.exe -m pip install --only-binary=:all: -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 7985 --reload
```

The normal backend health endpoint is available at http://localhost:7985/health.

If you see `WinError 10048`, port `7985` is already occupied, usually because this backend is already running. Do not start a second copy. To install dependencies, use the full requirements file command; never use `pip install ...` literally:

```powershell
.\.venv\Scripts\python.exe -m pip install --only-binary=:all: -r requirements.txt
```

For a duplicate-safe start, run this from the backend folder:

```powershell
.\start_backend.ps1
```
