from genericpath import exists
from re import X
import requests
import colorama
import os
import fade 
import time
import shutil
from py7zr import unpack_7zarchive
from distutils.log import error
from importlib.resources import path
from time import sleep
from turtle import clear


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def dl():
    clear()
    print(f"Paste your Path! eg. C:/Users/NexusAPI/Desktop/FiveM | *add the Name at the end! In this case its FiveM")
    path = input('> ')
    if os.path.exists(path):
        print(f"Path already exists. Exiting...")
        time.sleep(5)
        exit()
    else:
        time.sleep(1)
    clear()
    print(f"Creating directory: "+path)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
        print(f"Exiting....")
        time.sleep(5)
        
    time.sleep(1)
    clear()
    print(f"Done!")
    time.sleep(1)
    clear()
    print("Downloading artifacts")
    Url = 'https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/5848-4f71128ee48b07026d6d7229a60ebc5f40f2b9db/server.7z'
    r = requests.get(Url, allow_redirects=True)
    open('server.7z', 'wb').write(r.content)
    time.sleep(1)
    clear()
    print(f"Done!")
    time.sleep(1)
    clear()
    print(f"Moving file")
    shutil.move("server.7z", path)
    os.chdir(path)
    time.sleep(1)
    clear()
    print(f"Done!")
    time.sleep(1)
    clear()
    print(f"Unpacking files")
    shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
    shutil.unpack_archive(path+'/server.7z', path+'/server')
    time.sleep(1)
    clear()
    print(f"Done!") 
    time.sleep(1)
    clear()
    print(f"Remove old zip archive")
    os.remove(path+'/server.7z')
    time.sleep(1)
    clear()
    print(f"Done!")
    with open(path+'/Install.txt', 'w') as f:
        f.write(f'''=============================================
Server successfully installed!
Any questions? Discord: NexusAPI#8060
github.com/NexusAPI
=============================================''')
    time.sleep(1)
    clear()
    print(f"You have successfully installed your Server. Have fun!")
    time.sleep(2)
    clear()
    print(f"Exiting...")
    time.sleep(2)
    exit()
                
def logo():
    colorama.deinit()
    os.system("mode con cols=135 lines=30")
    os.system("title FiveM installer")
    clear()
    print(fade.pinkred(f'''
 ___           _        _ _
|_ _|_ __  ___| |_ __ _| | | ___ _ __
 | || '_ \/ __| __/ _` | | |/ _ \ '__|
 | || | | \__ \ || (_| | | |  __/ |
|___|_| |_|___/\__\__,_|_|_|\___|_|
                        by NexusAPI
'''))

    



if __name__ == '__main__':
    def menu():
        logo()
        print(f"[1] Install Files for Windows")
        print(f"[2] Install MySQL [DATABASE]")
        print(f"[3] Exit")
        
        ans = input('> ')
        
        if ans == "1":
            dl()
        elif ans == "2":
            print(f"In progress... Follow this: https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html")
            time.sleep(100)
            exit()
        elif ans == "3":
            print("[INFO] Exiting...")
            time.sleep(2)
            exit()
        else: 
            print("[INFO] Invalid input! Exiting...")
            time.sleep(2)
            exit()

menu()