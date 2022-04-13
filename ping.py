import os
import platform
import time
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

current_os = platform.system().lower()
site = "www.google.com"
exit_code = 1
wait_for = 60

if current_os == "windows":
    parameter = "-n"
else:
    parameter = "-c"


def check_status():
    exit_code = os.system(f"ping {parameter} 3 {site}>nul")
    now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    if exit_code == 1:
        print(f"{now} - {site} is offline")
        #messagebox.showinfo(f"{site}", f"{now} - {site} is offline")
    else:
        print(f"{now} - {site} is online")


while True:
    check_status()
    time.sleep(wait_for)
