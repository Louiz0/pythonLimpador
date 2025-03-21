from app import *

main_window = tk.Tk()
main_window.title("Limpador")
main_window.geometry("500x200")
main_window.resizable(0, 0)

# FUNCTIONS
# OPEN NEW WINDOW

def open_new_window():
    new_window = Toplevel(main_window)
    new_window.title("Janela de Seleção")
    new_window.geometry("175x100")
    new_window.resizable(0, 0)
    new_window.overrideredirect(1)
    
    label_type_number = ttk.Label (
    new_window, text = "Digite um número: ", font = "Helvetica 10 bold"
    )
    label_type_number.pack()
    
    entry_type_number = ttk.Entry(new_window)
    entry_type_number.pack()
    
    button_submit_number = ttk.Button (
        new_window, text = "OK", command = lambda: [get_number(),new_window.destroy()]
    )
    button_submit_number.pack()
    
    def get_number():
        number = entry_type_number.get()
        number = int(number)
        timed_folder_cleanup(number)

# LABELS
label_main_text = ttk.Label (
    text = "Selecione qual limpeza você deseja realizar", font = "Helvetica 14 bold"
)
label_main_text.place(x = 50, y = 0)

label_version = ttk.Label (
    text = "0.0.5", font = "Helvetica 10 bold"
)
label_version.place(x = 10, y = 180)

label_selected_cleanup = ttk.Label (
    text = "Limpeza por Pasta Selecionada", font = "Helvetica 10 bold"
)
label_selected_cleanup.place(x = 30, y = 30)

label_timed_folder_cleanup = ttk.Label (
    text = "Limpeza por Data", font = "Helvetive 10 bold"
)
label_timed_folder_cleanup.place(x = 320, y = 30)

# BUTTONS
button_clear_folders = ttk.Button (
    main_window, text = "Escolher pasta", command = selected_folder_cleanup
)
button_clear_folders.place(x = 80, y = 55, width = 100, height = 50)

button_timed_cleanup_folders = ttk.Button (
    main_window, text = "Escolher pasta", command = open_new_window
)
button_timed_cleanup_folders.place(x = 320, y = 55, width = 120, height = 50)

# MAIN IMAGE
image_main = Image.open("./images/png_limpador.png")
image_main_reduced = image_main.resize((38, 30), Image.Resampling.BICUBIC)
image_logo = ImageTk.PhotoImage(image_main_reduced)
label_image_logo = tk.Label (
    main_window, image = image_logo
)
label_image_logo.place(x = 435, y = 160)

# APP ICON
main_window.iconphoto(False, tk.PhotoImage(file = "./images/png_limpador.png"))

main_window.mainloop()