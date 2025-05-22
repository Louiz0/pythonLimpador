import urllib.request
import requests
from tkinter import messagebox
import os

URL = ("https://raw.githubusercontent.com/Louiz0/pythonLimpador/refs/heads/main/version.txt")
URL_new_version = urllib.request.urlopen(URL)

with open("version.txt", encoding='utf-8') as file:
    old_data = file.read()

new_data = URL_new_version.read().decode("utf-8")

def search_updates():
    if old_data != new_data:
        need_update(new_data, URL)

def need_update(new_data_variable, new_version_URL):
    print(new_data_variable)
    os.system("taskkill /f /im app.exe")

    resposta = requests.get(new_version_URL)
    file = open("version.txt", "w")
    file.write(resposta.text)

    messagebox.showinfo("Nova versão disponível", "O programa entrou em modo de atualização e será fechado. Após a conclusão será necessário reabrir.")

    new_version = requests.get(f"https://github.com/Louiz0/pythonLimpador/releases/download/{new_data_variable}/app.exe")
    open("app.exe", "wb").write(new_version.content)

if __name__ == "__main__":
    search_updates()