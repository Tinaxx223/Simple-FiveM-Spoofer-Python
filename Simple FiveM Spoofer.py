# (c) Tinnaxx (https://github.com/Tinaxx223)

import os
from os import path
import colorama
from colorama import Fore, Back, Style
import art
from art import *
import shutil
import requests
import subprocess
import time


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Welcome back, " + os.getlogin())
time.sleep(2)
clearconsole()

pathdDigitalEntitlements = os.getenv('LOCALAPPDATA') + "\DigitalEntitlements"

pathCitizenFX = os.getenv('APPDATA') + "\CitizenFX"

def main():
        if path.exists(pathdDigitalEntitlements):
            print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Removing account...")
            time.sleep(2)
            shutil.rmtree(pathdDigitalEntitlements)
            print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Removed!")
            time.sleep(2)
        else:
            print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.RED}We couldnt find an account")
            time.sleep(3)
        if path.exists(pathCitizenFX):
            print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Spoofing bans from servers...")
            time.sleep(2)
            filelist = [ f for f in os.listdir(pathCitizenFX) if f.endswith("gta5_settings.xml") ]
        for f in filelist:
            os.remove(os.path.join(pathCitizenFX, f))
            print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Spoofed")
            time.sleep(2)
        else:
            print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Spoof already done.")
            time.sleep(5)
main()
