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

def selected_folder_cleanup():
    file_path = filedialog.askdirectory()

    if not file_path:
        messagebox.showwarning("Alerta", "Nenhuma pasta foi selecionada")
        return
    
    try:
        for item in os.listdir(file_path):
            item_path = os.path.join(file_path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception:
                messagebox.showerror("Erro", "Erro ao apagar arquivos/pastas")

        messagebox.showinfo("Operação concluida!", "Limpeza concluida, arquivos que estavam abertos não podem ser limpos e restaram!")

    except Exception:
        messagebox.showerror("Erro", "Erro geral na operação")

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