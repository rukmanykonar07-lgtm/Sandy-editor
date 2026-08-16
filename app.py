import os
import subprocess

# Configure Puppeteer & HF server environment
os.environ["PUPPETEER_EXECUTABLE_PATH"] = "/usr/bin/chromium"
os.environ["PUPPETEER_SKIP_CHROMIUM_DOWNLOAD"] = "true"
os.environ["PORT"] = "7860"
os.environ["HOST"] = "0.0.0.0"

print("Installing npm dependencies...")
subprocess.run(["npm", "install"], check=True)

print("Starting OpenChatCut server on port 7860...")
subprocess.run(["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "7860"])
