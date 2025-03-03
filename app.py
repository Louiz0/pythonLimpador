import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import datetime
import time
from gui import *

# today = datetime.date.today()  # hoje
# selected_days = today - datetime.timedelta(days=3)  # + de 3 dias
# converted_days = time.mktime(selected_days.timetuple())

def selected_folder_cleanup():
    file_path = filedialog.askdirectory()
    for root, _, filenames in os.walk(file_path):
        for filename in filenames:
            new_file_path = os.path.join(root, filename)
            os.remove(new_file_path)

def timed_folder_cleanup(number):
    today = datetime.date.today() # hoje
    selected_days = today - datetime.timedelta(days = number) # escolher o dia
    converted_days = time.mktime(selected_days.timetuple()) # convertido em timestamp
    
    file_path = filedialog.askdirectory()
    for root, _, filenames in os.walk(file_path):
        for filename in filenames:
            new_file_path = os.path.join(root, filename)
            creation_date = os.path.getmtime(new_file_path)
            
            if creation_date < converted_days:
                os.remove(new_file_path)
                print(converted_days)
                print(creation_date)