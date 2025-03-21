import urllib.request
import requests
from tkinter import messagebox
import os

URL_new_version = urllib.request.urlopen("https://raw.githubusercontent.com/Louiz0/pythonLimpador/refs/heads/main/new_version.txt")
URL_old_version = "https://raw.githubusercontent.com/Louiz0/pythonLimpador/refs/heads/main/old_version.txt"

with open("old_version.txt", encoding='utf-8') as file:
    old_data = file.read()

new_data = URL_new_version.read().decode("utf-8")

def search_updates():
    if old_data != new_data:
        need_update(new_data, URL_old_version)

def need_update(new_data_variable, old_data_variable):
    os.system("taskkill /f /im app.exe")
    resposta = requests.get(old_data_variable)
    file = open("old_version.txt", "w")
    file.write(resposta.text)
    messagebox.showinfo("NOVA VERSÃO!", "NOVA VERSÃO ENCONTRADA, ATUALIZANDO... SERÁ NECESSARIO ABRIR O PROGRAMA NOVAMENTE")
    new_version = requests.get(f"https://github.com/Louiz0/pythonLimpador/releases/download/{new_data_variable}/app.exe")
    open("app.exe", "wb").write(new_version.content)

if __name__ == "__main__":
    search_updates()