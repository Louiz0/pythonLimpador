import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Toplevel
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
    
    file_path_prefetch = "C:\\Windows\\Prefetch"
    file_path_temp = "C:\\Windows\\Temp"
    file_path_user_temp = os.environ.get('TEMP')
    
    for path in [file_path_prefetch, file_path_temp, file_path_user_temp]:
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path, ignore_errors=True)
                except Exception as e:
                    print(f"Erro ao excluir {item_path}: {e}")
        except Exception as e:
            print(f"Erro ao listar {path}: {e}")
    messagebox.showinfo("Operação concluída", "Limpeza concluída. Alguns arquivos podem não ter sido removidos pois estavam em uso ou protegidos.")