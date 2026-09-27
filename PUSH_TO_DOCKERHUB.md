# Push images to Docker Hub

Run these yourself in PowerShell (needs your Docker Hub credentials — not something I run for you).

```powershell
# 1. Log in (use your Docker Hub username 104681360 and password, or better, a Personal Access Token
#    from hub.docker.com > Account Settings > Security > New Access Token)
docker login -u 104681360

# 2. Push each image
docker push 104681360/task42-flask-app:1.0
docker push 104681360/task43-webapp:1.0
docker push 104681360/task44-cli-tool:1.0
```

## Screenshots to capture for the report

- `docker login` success message.
- Each `docker push` output (shows layers pushing + digest).
- The Docker Hub website (hub.docker.com/repositories/104681360) showing all 3 repositories listed.
- Click into `task42-flask-app` repo on the website to show the tag `1.0` and pull command.

## Multi-host verification (Credit level requirement)

To satisfy "pull and run it on a secondary Docker host", you have two options:

1. **A second physical/VM machine** with Docker installed — run:
   ```powershell
   docker pull 104681360/task42-flask-app:1.0
   docker run -d -p 5000:5000 104681360/task42-flask-app:1.0
   ```
2. **Simulate a second host on the same machine** — remove the local image first so it's forced
   to actually pull from Docker Hub (not just reuse the local cache), which still demonstrates the
   registry round-trip:
   ```powershell
   docker rmi 104681360/task42-flask-app:1.0
   docker pull 104681360/task42-flask-app:1.0
   docker run -d -p 5001:5000 104681360/task42-flask-app:1.0
   ```
   Note in your report that this simulates a second host by forcing a fresh pull from the registry
   (be honest about this in the write-up — markers care that you understand the concept).

A real second host (a cloud VM, WSL2 distro treated as a separate Docker engine, or a friend's
machine) is stronger evidence if you have access to one.
