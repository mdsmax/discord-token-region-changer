import requests
from colorama import Fore
import os
import time

url = "https://ptb.discord.com/api/v9/users/@me/settings-proto/1"
brasil = "Yg4KBwoFcHQtQlISAwi0AQ=="
ing = "Yg4KBwoFZW4tVVMSAwi0AQ=="
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

with open("tokens.txt", "r") as file:
    tokens = file.read().splitlines()

def menu():
    os.system('cls')
    print("opções:\n1 - alterar para brasileiro\n2 - alterar para ingles")
    choice = input("> ")
    if choice == "1":
        for token in tokens:
            alterar(token, 1)
    elif choice == "2":
        for token in tokens:
            alterar(token, 2)
    else:
        os.system('cls')
        print("escreveu errado seu burro")
        time.sleep(1)
        menu()

def alterar(token, idioma: int):
    headers = {
        "cookie": "__dcfduid=e1e76090c95e11eeb80407c58e8b5018; __sdcfduid=e1e76091c95e11eeb80407c58e8b5018940091cc93bab511da545efa90b87b5627b93796364c9e08ac9ac959b82cb840; __stripe_mid=5aefd230-80fa-4da8-80a9-6fb9cc076a1589414d; cf_clearance=dAvDKUkShk1qZYEVAi5hDM4AMAmUg9gA_SliQHvrPCo-1709930570-1.0.1.1-OA8siXAp0g5C8OvJPm2BUS8VGhBhzXKiXgx8rGbQOKKnSJ2O.JUgXbqFF3_r4hgW2jX6XcLmQTFCPcPkk1BrEA; _cfuvid=INK.eu7CrW.ZL6gjBnEjbiXTvfPf4zXDVjEy7ZnWR9w-1709991633718-0.0.1.1-604800000; __cfruid=4f7cce2c9c92a40d418bd44abc899dd8f70994ca-1709991645; locale=pt-BR",
        "authorization": token,
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1059 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDU5Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6InB0LUJSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjEwNTkgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNzM3NjAsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ0ODY4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }
    if idioma == 1:
        payload = {"settings": brasil}
        msg = "brasileiro"
    else:
        payload = {"settings": ing}
        msg = "inglês"
    response = requests.request("PATCH", url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"{green}[SUCESSO]{reset} Token: {Fore.CYAN}{token[:30]}***{reset} teve seu idioma alterado para: {msg}")
    else:
        print(f"{red}[ERRO]{reset} Token: {Fore.CYAN}{token[:30]}***{reset} não teve seu idioma alterado | {response.json}")

os.system('cls')
menu()