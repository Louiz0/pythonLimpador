import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import datetime
import shutil
import time
from gui import *

os.startfile("updater.exe")

def timed_folder_cleanup(number):
    today = datetime.date.today() # hoje
    selected_days = today - datetime.timedelta(days = number) # escolher o dia
    converted_days = time.mktime(selected_days.timetuple()) # convertido em timestamp
    
    file_path = filedialog.askdirectory()

    if not file_path:
        messagebox.showwarning("Alerta", "Nenhuma pasta foi selecionada")

    for item in os.listdir(file_path):
        item_path = os.path.join(file_path, item)
        creation_date = os.path.getmtime(item_path)
            
        if creation_date < converted_days:
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception:
                messagebox.showwarning("Erro", "Erro geral na operação")
                
def windows_cache_cleanup():
    current_user = os.getlogin()
    
    file_path_prefetch, file_path_temp, file_path_user_temp = "C:\\Windows\\Prefetch", "C:\\Windows\\Temp", f"C:\\Users\\{current_user}\\AppData\\Local\\Temp\\*"
    
    try:
        for item in os.listdir(file_path_prefetch):
            item_path_prefetch = os.path.join(file_path_prefetch, item)
            
            if os.path.isfile(item_path_prefetch) or os.path.islink(item_path_prefetch):
                os.remove(item_path_prefetch)
            elif os.path.isdir(item_path_prefetch):
                shutil.rmtree(item_path_prefetch)
        
        for item in os.listdir(file_path_temp):
            item_path_temp = os.path.join(file_path_temp, item)
            
            if os.path.isfile(item_path_temp) or os.path.islink(item_path_temp):
                os.remove(item_path_temp)
            elif os.path.isdir(item_path_temp):
                shutil.rmtree(item_path_temp)

        for item in os.listdir(file_path_user_temp):
            item_path_user_temp = os.path.join(file_path_user_temp, item)
            
            try:
                if os.path.isfile(item_path_user_temp) or os.path.islink(item_path_user_temp):
                    os.remove(item_path_user_temp)
                elif os.path.isdir(item_path_user_temp):
                    shutil.rmtree(item_path_user_temp)
            except OSError:
                pass
    except OSError:
        pass
    
    print(file_path_user_temp)
    messagebox.showinfo("Operação concluida!", "Limpeza concluida, arquivos que estavam abertos não podem ser limpos e restaram!")