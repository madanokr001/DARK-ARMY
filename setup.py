# Author : cybermad

# setup

import os

def DARK_ARMY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r""" 
        
[01] | pip
[02] | pip3
   """)
    
DARK_ARMY()
select = input("""
┌──(root@DARK-4RMY)-[/home/setup]
└─# """)
    
if select == "1":
    os.system("pip install discord-webhook")
    os.system("pip install pynput")
    os.system("pip install pyautogui")
    os.system("pip install threading")
    os.system("pip install os")
    os.system("pip install shutil")
    os.system("pip install sys")
    os.system("pip install io")
    os.system("pip install pystyle")
    os.system("python darkarmy.py")

elif select == "2":
    os.system("pip3 install discord-webhook")
    os.system("pip3 install pynput")
    os.system("pip3 install pyautogui")
    os.system("pip3 install threading")
    os.system("pip3 install os")
    os.system("pip3 install shutil")
    os.system("pip3 install sys")
    os.system("pip3 install io")
    os.system("pip install pystyle")
    os.system("python darkarmy.py")
    

