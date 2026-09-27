# Exposing Task 4.3 publicly with ngrok

1. Sign up for a free account at https://dashboard.ngrok.com/signup and grab your authtoken from
   https://dashboard.ngrok.com/get-started/your-authtoken.

2. Install ngrok (Windows):
   ```powershell
   winget install ngrok.ngrok
   ```
   or download the zip from https://ngrok.com/download and put `ngrok.exe` somewhere on your PATH.

3. Add your authtoken once:
   ```powershell
   ngrok config add-authtoken <YOUR_AUTHTOKEN>
   ```

4. Run the Task 4.3 container locally (if not already running):
   ```powershell
   cd task4.3-webapp
   docker run -d --name task43-webapp -p 8080:8080 -e APP_TITLE="My Docker Task Tracker" 104681360/task43-webapp:1.0
   ```

5. Start the tunnel, pointing at the container's published port:
   ```powershell
   ngrok http 8080
   ```
   ngrok will print a public URL like `https://abcd1234.ngrok-free.app` — this is what you put in
   the report as the "Publicly Accessible URL" and what markers will open to verify the app live.

6. Keep the `ngrok http 8080` terminal window open during grading — closing it kills the tunnel.
   The free plan's URL changes every time you restart ngrok, so re-run step 5 (and update the
   report's URL) shortly before submission/grading if the session was closed.

## Screenshots to capture

- The `ngrok http 8080` terminal showing the "Forwarding" line with the public https URL.
- The web app opened in a browser at that public https URL, showing it's the containerized app
  (not localhost) — the browser address bar must clearly show the ngrok domain.
- `docker ps` showing the container running and its port mapping alongside the ngrok tunnel.
