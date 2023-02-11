import os, platform, subprocess

def check():
    r = os.system("pip3 install discord_webhook")
    if(r == 1):
        r = os.system("pip install discord_webhook")
        if(r == 1):
            from urllib import request
            if(platform.system == "Windows"):
                remote_url = 'https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe'
                local_file = '''%appdata%\\python-3.11.1-amd64.exe'''
                request.urlretrieve(remote_url, local_file)
                process = subprocess.Popen(local_file, shell=True, stdin=subprocess.PIPE)
                path = os.path.join(location="%appdata%", file="python-3.11.1-amd64.exe")
                os.remove(path)
                print("please, restart the program...")
                exit()
            elif (platform.system == "Linux"):
                s = os.system("sudo apt install python3 -y")
                if(s == 1):
                    s = os.system("sudo pacman -S python3 -y")
                    if(s == 1):
                        os.system("sudo yum install python3 -y")
                        exit()
                    else:
                        exit()
                else:
                    exit()
        else:
            os.system("pip install requests")
            os.system("pip install discord")
            os.system("pip install opencv-python")
            os.system("pip install pytube")
            os.system("pip install pyautogui")
            os.system("pip install Pillow")
    else:
        os.system("pip3 install requests")
        os.system("pip3 install discord")
        os.system("pip3 install opencv-python")
        os.system("pip3 install pytube")
        os.system("pip3 install pyautogui")
        os.system("pip3 install Pillow")
    if(platform.system() == "Linux"):
        l = os.system("sudo apt-get install scrot -y")
        if(l == 1):
            r = os.system("sudo pacman -S scrot -y")
            if(r == 1):
                os.system("sudo yum install scrot -y")
    os.system("cls||clear")
