# Synora AI

Synora AI is a hackathon-ready prototype for athlete cognitive readiness screening using eye movement and cognitive assessment patterns.

## Problem statement

“AI in Concussion Detection – Enable rapid screening through eye movement and cognitive analysis.”

This project demonstrates a preliminary screening workflow for research and demo purposes only. It does not diagnose concussion or replace professional medical care.

## Safety disclaimer

> “This tool is for preliminary screening and educational purposes only. It does not replace professional medical evaluation.”

## Architecture

- React frontend with Vite
- FastAPI backend
- SQLite database
- Python feature extraction and ML scoring
- Prototype eye tracking and cognitive test flow

## Technology stack

- React
- Vite
- JavaScript
- FastAPI
- SQLite
- Python
- NumPy
- Pandas
- OpenCV
- MediaPipe (available when environment supports it)
- scikit-learn

## Installation

### Frontend

```bash
cd "C:\sandhiya project\NeuroGuardAI\frontend"
npm install
npm run dev
```

### Backend

```bash
cd "C:\sandhiya project\NeuroGuardAI\backend"
python -m venv .venv
.\.venv\Scripts\python.exe -m ensurepip --upgrade
.\.venv\Scripts\python.exe -m pip install --only-binary=:all: -r backend\requirements-full.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 7985 --reload
```

After the first start, use `backend\start_backend.ps1` to avoid starting a duplicate server on port `7985`.

Set the API URL in the frontend:

```bash
VITE_API_URL=http://localhost:7985
```

### Vercel deployment

The root `requirements.txt` is intentionally lightweight for Vercel's serverless function size limit. The deploy entrypoint is `api/index.py`; the local full ML/computer-vision stack remains available through `backend\requirements-full.txt`.

## Troubleshooting on Windows PowerShell

- If port `7985` reports `WinError 10048`, the backend is already running. Use `http://localhost:7985/health` instead of starting another server.
- Do not run `pip install ...`; the three dots are not a package name. Use the complete requirements command:

```powershell
.\.venv\Scripts\python.exe -m pip install --only-binary=:all: -r backend\requirements-full.txt
```
- After installing Git, close and reopen the VS Code terminal so the `git` command is added to PATH. In the current terminal, use `$env:Path = "C:\Program Files\Git\cmd;" + $env:Path` as a temporary refresh.

## Demo flow

1. Home
2. Profile
3. Symptoms
4. Eye movement test
5. Reaction test
6. Memory test
7. Attention test
8. Analysis
9. Results dashboard
10. Assessment history
11. Report download

## Current limitations

- This is a prototype only.
- It is not a clinically validated diagnostic tool.
- Eye tracking is demo-mode when webcam or tracking dependencies are unavailable.
- The ML pipeline uses prototype training data and should be replaced with a validated clinical dataset before any real-world use.

## Future improvements

- integrate validated clinical datasets
- add explainable model outputs
- add CSV export
- add more precise eye tracking metrics and gaze estimation
- improve results dashboard and clinician reporting

## License

Educational prototype for hackathon use only.
