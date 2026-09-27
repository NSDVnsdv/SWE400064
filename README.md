# SWE40006 Deployment Task 4 — Container Application Deployment & Orchestration using Docker

Source code and Dockerfiles supporting the Deployment Task 4 report (Pass through High Distinction).

## Structure

- `task4.2-flask-app/` — Task 4.2 (Credit): basic Flask app, listens on port 5000.
- `task4.3-webapp/` — Task 4.3 (Distinction): custom Flask "Task Tracker" web app with an
  optimized multi-stage Dockerfile (non-root user, gunicorn, healthcheck), listens on port 8080.
- `task4.4-cli-tool/` — Task 4.4 (High Distinction): non-web CLI tool (word-frequency analyzer)
  that reads/writes via mounted Docker volumes and exits after completing its job.
- `PUSH_TO_DOCKERHUB.md` — commands used to tag/push/pull images across Docker Hub.
- `PUBLIC_ACCESS_NGROK.md` — steps used to expose Task 4.3 publicly via ngrok.
- `report/` — the submitted report document.

## Docker Hub images

- `104681360/task42-flask-app:1.0`
- `104681360/task43-webapp:1.0`
- `104681360/task44-cli-tool:1.0`

## Quick start

Each subfolder is a self-contained Docker build context:

```powershell
cd task4.2-flask-app
docker build -t task42-flask-app:local .
docker run -d -p 5000:5000 task42-flask-app:local

cd ../task4.3-webapp
docker build -t task43-webapp:local .
docker run -d -p 8080:8080 -e APP_TITLE="My Docker Task Tracker" task43-webapp:local

cd ../task4.4-cli-tool
docker build -t task44-cli-tool:local .
docker run --rm -v "${PWD}/sample-input:/data/input:ro" -v "${PWD}/output:/data/output" task44-cli-tool:local
```
