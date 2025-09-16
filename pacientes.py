import tkinter as tk
from tkinter import ttk, messagebox
import oracledb

# =============================
# Conexión a Oracle
# =============================
conn = oracledb.connect(
    user="system",
    password="Tapiero123",
    dsn="localhost:1521/orcl"  # Cambiar según tu instancia
)
cursor = conn.cursor()

# =============================
# Funciones CRUD
# =============================
def crear_paciente():
    try:
        sql = """INSERT INTO PACIENTES (NOMBRE, EDAD, GENERO, TELEFONO, DIRECCION)
                 VALUES (:1, :2, :3, :4, :5)"""
        cursor.execute(sql, (
            entry_nombre.get(),
            int(entry_edad.get()) if entry_edad.get() else None,
            entry_genero.get(),
            entry_telefono.get(),
            entry_direccion.get()
        ))
        conn.commit()
        messagebox.showinfo("Éxito", "✅ Paciente creado correctamente.")
        leer_pacientes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def leer_pacientes():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT ID, NOMBRE, EDAD, GENERO, TELEFONO, DIRECCION, FECHA_REGISTRO FROM PACIENTES")
    for paciente in cursor.fetchall():
        tree.insert("", tk.END, values=paciente)

def actualizar_paciente():
    try:
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un paciente para actualizar.")
            return
        valores = tree.item(seleccionado)["values"]
        id_paciente = valores[0]

        sql = """UPDATE PACIENTES SET NOMBRE=:1, EDAD=:2, GENERO=:3, TELEFONO=:4, DIRECCION=:5
                 WHERE ID=:6"""
        cursor.execute(sql, (
            entry_nombre.get(),
            int(entry_edad.get()) if entry_edad.get() else None,
            entry_genero.get(),
            entry_telefono.get(),
            entry_direccion.get(),
            id_paciente
        ))
        conn.commit()
        messagebox.showinfo("Éxito", "✅ Paciente actualizado correctamente.")
        leer_pacientes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_paciente():
    try:
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un paciente para eliminar.")
            return
        valores = tree.item(seleccionado)["values"]
        id_paciente = valores[0]

        cursor.execute("DELETE FROM PACIENTES WHERE ID=:1", (id_paciente,))
        conn.commit()
        messagebox.showinfo("Éxito", "✅ Paciente eliminado correctamente.")
        leer_pacientes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# =============================
# Interfaz gráfica con Tkinter
# =============================
root = tk.Tk()
root.title("🏥 Gestión de Pacientes (IPS)")
root.geometry("900x600")

# Frame de formulario
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame_form, width=30)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_form, text="Edad:").grid(row=1, column=0, sticky="e")
entry_edad = tk.Entry(frame_form, width=30)
entry_edad.grid(row=1, column=1)

tk.Label(frame_form, text="Género:").grid(row=2, column=0, sticky="e")
entry_genero = tk.Entry(frame_form, width=30)
entry_genero.grid(row=2, column=1)

tk.Label(frame_form, text="Teléfono:").grid(row=3, column=0, sticky="e")
entry_telefono = tk.Entry(frame_form, width=30)
entry_telefono.grid(row=3, column=1)

tk.Label(frame_form, text="Dirección:").grid(row=4, column=0, sticky="e")
entry_direccion = tk.Entry(frame_form, width=30)
entry_direccion.grid(row=4, column=1)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_crear = tk.Button(frame_botones, text="➕ Crear", command=crear_paciente, width=12, bg="lightgreen")
btn_crear.grid(row=0, column=0, padx=5)

btn_leer = tk.Button(frame_botones, text="📋 Leer", command=leer_pacientes, width=12, bg="lightblue")
btn_leer.grid(row=0, column=1, padx=5)

btn_actualizar = tk.Button(frame_botones, text="✏️ Actualizar", command=actualizar_paciente, width=12, bg="khaki")
btn_actualizar.grid(row=0, column=2, padx=5)

btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", command=eliminar_paciente, width=12, bg="salmon")
btn_eliminar.grid(row=0, column=3, padx=5)

# Tabla de pacientes
columns = ("ID", "Nombre", "Edad", "Género", "Teléfono", "Dirección", "Fecha Registro")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
tree.pack(fill=tk.BOTH, expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

# Inicializar tabla
leer_pacientes()

root.mainloop()
