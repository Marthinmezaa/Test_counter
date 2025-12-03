import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Gestor de Pruebas - Poligrafia')
app.geometry('800x500')

# --- Create buttons ---
new_test_bttm = ctk.CTkButton(
    master=app,
    text='Nuevo test',
    width=200,
    height=50
)

list_test_bttm = ctk.CTkButton(
    master=app,
    text='Listar pruebas',
    width=200,
    height=50
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

# ----------------------
# Open new test
# ----------------------
def open_new_test_form():
    form_window = ctk.CTkToplevel(app)
    form_window.title('Nueva Prueba')
    form_window.geometry('400x400')

    ctk.CTkLabel(master=form_window, text='Numero de legajo:').place(x=20, y=20)
    file_entry = ctk.CTkEntry(form_window)
    file_entry.place(x=150, y=50)

    ctk.CTkLabel(master=form_window, text='Tipo de prueba:').place(x=20, y=60)
    type_file_entry = ctk.CTkEntry(master=form_window)
    type_file_entry.place(x=150, y=60)

    ctk.CTkLabel(master=form_window, text='Empresa:').place(x=20, y=100)
    company_type = ctk.CTkEntry(master=form_window)
    company_type.place(x=150, y=100)

    ctk.CTkLabel(master=form_window, text='Fecha:').place(x=20, y=140)
    date_type = ctk.CTkEntry(master=form_window)
    date_type.place(x=150, y=140)

    ctk.CTkLabel(master=form_window, text='Cantidad de sujetos:').place(x=20, y=180)
    number_subjects = ctk.CTkEntry(master=form_window)
    number_subjects.place(x=150, y=180)

    






app.mainloop()