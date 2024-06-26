import requests, commands.settings
from colorama import Fore


def internetStatus():
    if commands.settings.online:
        try:
            response = requests.get("https://google.com/", timeout=5)
            return True
        except requests.ConnectionError:
            return False
    else:
        return False


def displayInternetStatus():
    if internetStatus():
        print("You are " + Fore.BLUE + "online" + Fore.GREEN)
    else:
        print("You are " + Fore.RED + "offline" + Fore.GREEN)
