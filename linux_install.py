import os

os.system("mkdir RAT")
os.system("mkdir RAT/Windows")
os.system("mkdir RAT/MacOS")
os.system("mkdir RAT/Linux")
os.system("mkdir temp")
os.system("mkdir temp/linux")
os.system("mkdir temp/macos")
os.system("mkdir temp/windows")
os.system("mkdir temp/listener")
os.system("mkdir temp/listener/windows")
os.system("mkdir temp/listener/macos")
os.system("mkdir temp/listener/linux")
os.system("mkdir temp/listener/")
os.system("python3 -m pip install colorama pyfiglet")
os.system("sudo python3 -m pip install colorama")
os.system("chmod +x ezsploit")
os.system("rm README.md")
os.system("clear")

from colorama import Fore, Style
from pyfiglet import figlet_format
print(Fore.GREEN + Style.BRIGHT + figlet_format("Done!", font = "smslant"))
print(Fore.YELLOW + Style.BRIGHT + "[!]\t" + Fore.WHITE + "ezsploit" + Fore.WHITE + Style.NORMAL)
print("")
