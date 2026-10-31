from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import threading
import time
import subprocess
import os

PORT = 8080

os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = f"http://127.0.0.1:{PORT}"

def open_browser():
    time.sleep(1)
    try:
        subprocess.Popen(["termux-open-url", url])
    except FileNotFoundError:
        print("Open Chrome:", url)

print("=" * 40)
print("       ROHIT IMAGE STUDIO PRO")
print("=" * 40)
print(f"Website: {url}")
print("Server started successfully!")
print("Press CTRL + C to stop.")

threading.Thread(
    target=open_browser,
    daemon=True
).start()

try:
    server = ThreadingHTTPServer(
        ("0.0.0.0", PORT),
        SimpleHTTPRequestHandler
    )
    server.serve_forever()

except KeyboardInterrupt:
    print("\nServer stopped!")
