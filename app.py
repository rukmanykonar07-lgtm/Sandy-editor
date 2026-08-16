import os
import subprocess
import urllib.request

# 1. Download and load Node.js v22 dynamically (bypasses system Node 18)
NODE_VERSION = "v22.14.0"
NODE_DIR = f"/home/user/node-{NODE_VERSION}-linux-x64"

if not os.path.exists(NODE_DIR):
    print(f"Downloading Node.js {NODE_VERSION}...")
    url = f"https://nodejs.org/dist/{NODE_VERSION}/node-{NODE_VERSION}-linux-x64.tar.xz"
    tar_path = "/tmp/node.tar.xz"
    urllib.request.urlretrieve(url, tar_path)
    print("Extracting Node.js...")
    subprocess.run(["tar", "-xf", tar_path, "-C", "/home/user"], check=True)

# Prepend Node 22 binaries to PATH
os.environ["PATH"] = f"{NODE_DIR}/bin:" + os.environ.get("PATH", "")

# 2. Environment configuration
os.environ["PUPPETEER_EXECUTABLE_PATH"] = "/usr/bin/chromium"
os.environ["PUPPETEER_SKIP_CHROMIUM_DOWNLOAD"] = "true"
os.environ["PORT"] = "7860"
os.environ["HOST"] = "0.0.0.0"
os.environ["ONNXRUNTIME_NODE_INSTALL_CUDA"] = "skip"

print("Active Node version:", subprocess.run(["node", "-v"], capture_output=True, text=True).stdout.strip())

print("Installing npm dependencies...")
subprocess.run(["npm", "install", "--legacy-peer-deps"], check=True)

print("Starting OpenChatCut server on port 7860...")
subprocess.run(["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "7860"])
