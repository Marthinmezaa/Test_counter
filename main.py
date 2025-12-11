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
# Open search tests
# ----------------------
def open_search_test():
    search_window = ctk.CTkToplevel(app)
    search_window.title('Buscar prueba')
    search_window.geometry('400x300')

    # --- Field to enter file number ---
    ctk.CTkLabel(master=search_window, text='Numero de legajo:').place(x=20, y=20)
    legajo_entry = ctk.CTkEntry(master=search_window)
    legajo_entry.place(x=150, y=20)

    # --- Area to display results ---
    result_box = ctk.CTkTextbox(master=search_window, width=350, height=200)
    result_box.place(x=20, y=100)

    # --- Function that performs the search ---
    def search_test():
        legajo = legajo_entry.get().strip()
        result_box.delete('0.0', 'end')

        if not legajo:
            result_box.insert('end', 'Por favor ingresa el numero de legajo.\n')
            return

        # --- Get results from the database ---
        tests = get_test_by_file_number(legajo)

        if not tests:
            result_box.insert('end', 'No se encontraron resultados.\n')
            return

        # --- Show results ---
        for test in tests:
            id, file_number, type_file, company_name, date_test, subjects_amount = test
            result_box.insert('end', f'ID: {id}\n')
            result_box.insert('end', f'Legajo: {file_number}\n')
            result_box.insert('end', f'Tipo: {type_file}\n')
            result_box.insert('end', f'Empresa: {company_name}\n')
            result_box.insert('end', f'Fecha: {date_test}\n')
            result_box.insert('end', f'Sujetos: {subjects_amount}\n')
            result_box.insert('end', '-----------------------\n')

    # --- Search button ---
    search_bttm = ctk.CTkButton(search_window, text='Buscar', command=search_test)
    search_bttm.place(x=150, y=60)

# ----------------------
# Open delete tests
# ----------------------
def open_delete_test():
    delete_window = ctk.CTkToplevel(app)
    delete_window.title('Eliminar prueba')
    delete_window.geometry('400x200')

    # --- ID Entry ---
    ctk.CTkLabel(master=delete_window, text='Ingrese el ID de la prueba a eliminar:').place(x=20, y=20)
    id_entry = ctk.CTkEntry(master=delete_window)
    id_entry.place(x=200, y=50)

    # --- Result ---
    result_label = ctk.CTkLabel(master=delete_window, text='')
    result_label.place(x=20, y=140)

    # --- Elimination logic ---
    def delete_action():
        test_id = id_entry.get().strip()

        if not test_id.isdigit():
            result_label.configure(text='ID invalido', text_color='red')
            return
        
        deleted = delete_test(int(test_id))

        if deleted == 0:
            result_label.configure(text='No existe registro con ese ID', text_color='red')
        else:
            result_label.configure(text='Prueba eliminada correctamente', text_color='green')

    # --- Button ---
    delete_button = ctk.CTkButton(
        master=delete_window,
        text='Eliminar',
        command=delete_action
    )
    delete_button.place(x=150, y=90)

# ----------------------
# Edit test
# ----------------------            
def open_edit_test():
    edit_window = ctk.CTkToplevel(app)
    edit_window.title('Editar prueba')
    edit_window.geometry('450x400')

    preview_label = ctk.CTkLabel(master=edit_window, text='', justify='left')
    preview_label.place(x=20, y=90)

    # --- ID Entry ---
    ctk.CTkLabel(master=edit_window, text='Ingrese ID de la prueba').place(x=20, y=20)
    id_entry = ctk.CTkEntry(master=edit_window)
    id_entry.place(x=200, y=20)

    # --- Button to load data ---
    def load_test():
        test_id = id_entry.get().strip()

        if not test_id.isdigit():
            messagebox.showerror('Error', 'El ID debe ser un numero entero')
            return
        
        result = get_test_by_id(int(test_id))
        if not result:
            messagebox.showerror('Error', 'No existe un registro con ese ID')
            return
        
        # --- Extract tuple ---
        _, file_n, t_type, company, date, subjects = result

        # --- Show preview ---
        preview_label.configure(
            text=f'ID: {test_id}\n'
                 f'Legajo: {file_n}\n'
                 f'Tipo de prueba: {t_type}\n'
                 f'Empresa: {company}\n'
                 f'Fecha: {date}\n'
                 f'Sujetos: {subjects}'   
        )

        # --- Load values ​​into the inputs ---
        file_entry.configure(state='normal')
        type_entry.configure(state='normal')
        company_entry.configure(state='normal')
        date_entry.configure(state='normal')
        subjects_entry.configure(state='normal')

        # --- Insert values ​​into the inputs ---
        file_entry.delete(0, 'end')
        file_entry.insert(0, file_n)

        type_entry.delete(0, 'end')
        type_entry.insert(0, t_type)

        company_entry.delete(0, 'end')
        company_entry.insert(0, company)

        date_entry.delete(0, 'end')
        date_entry.insert(0, date)

        subjects_entry.delete(0, 'end')
        subjects_entry.insert(0, subjects)

        # --- Save changes button --- 
        save_button.configure(state='normal')

    load_button = ctk.CTkButton(master=edit_window, text='Cargar datos', command=load_test)
    load_button.place(x=200, y=60)

    # --- Editable fields ---
    ctk.CTkLabel(master=edit_window, text='Legajo:').place(x=20, y=120)
    file_entry = ctk.CTkEntry(master=edit_window, state='disabled')
    file_entry.place(x=200, y=120)

    ctk.CTkLabel(master=edit_window, text='Tipo de prueba:').place(x=20, y=160)
    type_entry = ctk.CTkEntry(master=edit_window, state='disabled')
    type_entry.place(x=200, y=160)    

    ctk.CTkLabel(master=edit_window, text='Empresa:').place(x=20, y=200)
    company_entry = ctk.CTkEntry(master=edit_window, state='disabled')
    company_entry.place(x=200, y=200)

    ctk.CTkLabel(master=edit_window, text='Fecha (YYYY-MM-DD)').place(x=20, y=240)
    date_entry = ctk.CTkEntry(master=edit_window, state='disabled')
    date_entry.place(x=200, y=240)

    ctk.CTkLabel(master=edit_window, text='Cantidad de sujetos:').place(x=20, y=280)
    subjects_entry = ctk.CTkEntry(master=edit_window, state='disabled')
    subjects_entry.place(x=200, y=280)

    # --- Button to save changes ---
    def save_changes():
        test_id = id_entry.get().strip()

        if not test_id.isdigit():
            messagebox.showerror('Error', 'ID invalido')
            return
        
        update = update_test(
            int(test_id),
            file_entry.get(),
            type_entry.get(),
            company_entry.get(),
            date_entry.get(),
            subjects_entry.get()
        )

        if update == 0:
            messagebox.showerror('Error', 'No se pudo actualizar. Verifique el ID sea el correcto.')
        else:
            messagebox.showinfo('Exito!', 'Prueba actualizada correctamente.')
            edit_window.destroy()

    save_button = ctk.CTkButton(master=edit_window, text='Guardar cambios', command=save_changes)
    save_button.place(x=140, y=330)

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
search_bttm = ctk.CTkButton(
    master=app,
    text='Buscar',
    width=200,
    height=50,
    command=open_search_test
)
delete_bttm = ctk.CTkButton(
    master=app,
    text='Eliminar legajo',
    width=200,
    height=50,
    command=open_delete_test
)
edit_test_bttm = ctk.CTkButton(
    master=app,
    text='Editar prueba',
    width=200,
    height=50,
    command=open_edit_test
)

# --- Locate buttons ---
new_test_bttm.place(x=50, y=50)
list_test_bttm.place(x=50, y=120)
search_bttm.place(x=50, y=190)
delete_bttm.place(x=50, y=260)
edit_test_bttm.place(x=50, y=330)


app.mainloop()