import customtkinter as ctk
from database import create_database, insert_test, get_all_test
from tkinter import messagebox

create_database()

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Gestor de Pruebas - Poligrafia')
app.geometry('800x500')

# ----------------------
# Open new test
# ----------------------
def open_new_test_form():
    form_window = ctk.CTkToplevel(app)
    form_window.title('Nueva Prueba')
    form_window.geometry('400x400')

    # --- Window fields ---
    ctk.CTkLabel(master=form_window, text='Numero de legajo:').place(x=20, y=20)
    file_entry = ctk.CTkEntry(master=form_window)
    file_entry.place(x=150, y=20)

    ctk.CTkLabel(master=form_window, text='Tipo de prueba:').place(x=20, y=60)
    type_file_entry = ctk.CTkEntry(master=form_window)
    type_file_entry.place(x=150, y=60)

    ctk.CTkLabel(master=form_window, text='Empresa:').place(x=20, y=100)
    company_type = ctk.CTkEntry(master=form_window)
    company_type.place(x=150, y=100)

    ctk.CTkLabel(master=form_window, text='Fecha (YYYY-MM-DD):').place(x=20, y=140)
    date_type = ctk.CTkEntry(master=form_window)
    date_type.place(x=150, y=140)

    ctk.CTkLabel(master=form_window, text='Cantidad de sujetos:').place(x=20, y=180)
    number_subjects = ctk.CTkEntry(master=form_window)
    number_subjects.place(x=150, y=180)

    # --- Function to save to the database ---
    def save_test():
        file_number = file_entry.get().strip()
        type_file = type_file_entry.get().strip()
        company_name = company_type.get().strip()
        date_test = date_type.get().strip()
        subjects_amount = number_subjects.get().strip()

        # --- Field validation ---
        if not file_number or not type_file or not company_name or not date_test or not subjects_amount:
            messagebox.showerror('Error', 'Todos los campos son obligatorios')
            return
        
        # --- Save to the database ---
        insert_test(file_number, type_file, company_name, date_test, subjects_amount)

        messagebox.showinfo('Exito', 'Prueba guardada correctamente')

         # --- Close window ---
        form_window.destroy()

    save_bttn = ctk.CTkButton(
        master=form_window,
        text='Guardar',
        width=100,
        height=40,
        command=save_test
    )

    save_bttn.place(x=150, y= 230)

# ----------------------
# Open list tests
# ----------------------
def open_list_tests():
    list_windows = ctk.CTkToplevel(app)
    list_windows.title('Listado de pruebas')
    list_windows.geometry('600x400')

    tests = get_all_test()

    if not tests:
        ctk.CTkLabel(list_windows, text='No hay pruebas registradas').pack(pady=20)
        return
    
    # --- Create a text box to display the data ---
    textbox = ctk.CTkTextbox(list_windows, width=550, height=350)
    textbox.pack(pady=10)

    for test in tests:
        id, file_number, type_file, company_name, date_test, subjects_amount = test

        textbox.insert('end', f'ID: {id}\n')
        textbox.insert('end', f'Legajo: {file_number}\n')
        textbox.insert('end', f'Tipo de prueba: {type_file}\n')
        textbox.insert('end', f'Empres: {company_name}\n')
        textbox.insert('end', f'Fecha: {date_test}\n')
        textbox.insert('end', f'Cantidad de sujetos: {subjects_amount}\n')
        textbox.insert('end', '-----------------------------\n')

# ----------------------
# Buttons and locate
# ----------------------
new_test_bttm = ctk.CTkButton(
    master=app,
    text='Nuevo test',
    width=200,
    height=50,
    command=open_new_test_form
)

list_test_bttm = ctk.CTkButton(
    master=app,
    text='Lista de pruebas',
    width=200,
    height=50,
    command=open_list_tests
)
search_bttm = ctk.CTkButton(
    master=app,
    text='Buscar',
    width=200,
    height=50
)

# --- Locate buttons ---
new_test_bttm.place(x=50, y=50)
list_test_bttm.place(x=50, y=120)
search_bttm.place(x=50, y=190)


app.mainloop()