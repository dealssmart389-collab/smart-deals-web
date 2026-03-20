import subprocess
import os

def send_secure_notification(title, message):
    termux_bin = "/data/data/com.termux/files/usr/bin/termux-notification"
    if os.path.exists(termux_bin):
        try:
            subprocess.run([termux_bin, "-t", title, "-c", message], check=True, shell=False)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Notification: {title} - {message}")

if __name__ == "__main__":
    send_secure_notification("Smart Deals", "تم تطهير الكود بنجاح 100%")
