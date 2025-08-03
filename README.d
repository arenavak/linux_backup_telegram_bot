# Telegram File Sender with System Report

This Python script sends a system status report (CPU, RAM, disk, and network usage) and then sends a specified file to a Telegram chat using a bot.

---

## 📦 Features

- Sends a message with:
  - Current date and time
  - Hostname and OS info
  - CPU usage
  - RAM usage
  - Disk usage
  - Network usage (sent & received)
- Sends any file to a Telegram chat
- Fully async, fast and lightweight

---

## 🚀 Requirements

- Python 3.10 or later

### Install Dependencies

```bash
pip install python-telegram-bot psutil
```

---

## ⚙️ Configuration

Edit the script (`backuper.py`) and update these variables:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"         # Your Telegram bot token
CHAT_ID = 123456789                        # Your Telegram chat ID (as an integer)
FILE_PATH = "path/to/your/file.txt"        # The file to send
```

---

## ▶️ How to Run

```bash
python3 backuper.py
```

---

You can also use it with `crontab` to back up your files automatically.
