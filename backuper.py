import asyncio
import platform
import psutil
import socket
import datetime
from telegram import Bot

# === Configuration ===
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = 123456789  # Replace with your chat ID
FILE_PATH = "path/to/your/file.txt"  # Replace with the path to your file


def get_system_info() -> str:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    system = platform.system()
    release = platform.release()
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()

    info = (
        f"🕒 Date & Time: {now}\n"
        f"💻 System: {system} {release}\n"
        f"🖥 Hostname: {hostname}\n"
        f"⚙️ CPU Usage: {cpu_percent}%\n"
        f"📊 RAM Usage: {ram.percent}% ({round(ram.used / 1e9, 2)} GB used)\n"
        f"💽 Disk Usage: {disk.percent}% ({round(disk.used / 1e9, 2)} GB used)\n"
        f"📡 Network Sent: {round(net_io.bytes_sent / 1e6, 2)} MB\n"
        f"📥 Network Received: {round(net_io.bytes_recv / 1e6, 2)} MB"
    )
    return info


async def send_report_and_file():
    bot = Bot(token=BOT_TOKEN)
    try:
        # Send system info text
        system_info = get_system_info()
        await bot.send_message(chat_id=CHAT_ID, text=system_info)

        # Send file
        with open(FILE_PATH, "rb") as file:
            await bot.send_document(chat_id=CHAT_ID, document=file)

        print("✅ Report and file sent successfully.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(send_report_and_file())
