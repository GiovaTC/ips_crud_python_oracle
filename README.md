# ips_crud_python_oracle

<img width="203" height="193" alt="image" src="https://github.com/user-attachments/assets/acd0ce8a-579d-497b-a76e-797430d0bb13" />    

# 🏥 CRUD en Python con Oracle (IPS - Pacientes)

<img width="2552" height="1079" alt="image" src="https://github.com/user-attachments/assets/42428113-bb9c-454f-8483-638aca476e7d" />

<img width="2558" height="1079" alt="image" src="https://github.com/user-attachments/assets/0d571769-8e61-414a-88ff-058b41a68b6c" />

<img width="2559" height="1041" alt="image" src="https://github.com/user-attachments/assets/4ffdeb4d-92e8-427c-b756-cab08e29c4d9" />

<img width="2552" height="1078" alt="image" src="https://github.com/user-attachments/assets/416d1408-66eb-4506-ad9b-97411846727a" />

Este proyecto implementa un **CRUD (Crear, Leer, Actualizar, Eliminar)** en **Python** conectado a una base de datos **Oracle**, utilizando la librería oficial [`oracledb`](https://python-oracledb.readthedocs.io/).
La entidad gestionada será **PACIENTES** de una **IPS (Institución Prestadora de Salud)**.

---

## 📌 1. Script SQL para crear la tabla en Oracle
```sql
CREATE TABLE PACIENTES (
    ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    NOMBRE VARCHAR2(100) NOT NULL,
    EDAD NUMBER(3),
    GENERO VARCHAR2(10),
    TELEFONO VARCHAR2(20),
    DIRECCION VARCHAR2(200),
    FECHA_REGISTRO TIMESTAMP DEFAULT SYSTIMESTAMP
);

📌 2. Instalación de la librería oracledb
Ejecuta en tu terminal:
bash
pip install oracledb
⚠️ Nota: Asegúrate de tener instalado Oracle Client o utilizar el modo Thin de oracledb.

📌 3. CRUD en Python (pacientes.py)
python

import oracledb

# Configura la conexión a Oracle
conn = oracledb.connect(
    user="usuario", 
    password="clave", 
    dsn="localhost:1521/XEPDB1"  # Cambiar según tu instancia
)
cursor = conn.cursor()

# =============================
# FUNCIONES CRUD
# =============================

def crear_paciente(nombre, edad, genero, telefono, direccion):
    sql = """INSERT INTO PACIENTES (NOMBRE, EDAD, GENERO, TELEFONO, DIRECCION) 
             VALUES (:1, :2, :3, :4, :5)"""
    cursor.execute(sql, (nombre, edad, genero, telefono, direccion))
    conn.commit()
    print("✅ Paciente creado correctamente.")

def leer_pacientes():
    sql = "SELECT ID, NOMBRE, EDAD, GENERO, TELEFONO, DIRECCION, FECHA_REGISTRO FROM PACIENTES"
    cursor.execute(sql)
    pacientes = cursor.fetchall()
    for p in pacientes:
        print(p)

def actualizar_paciente(id_paciente, nombre=None, edad=None, genero=None, telefono=None, direccion=None):
    sql = "UPDATE PACIENTES SET "
    campos = []
    valores = []
    
    if nombre:
        campos.append("NOMBRE = :1")
        valores.append(nombre)
    if edad:
        campos.append("EDAD = :2")
        valores.append(edad)
    if genero:
        campos.append("GENERO = :3")
        valores.append(genero)
    if telefono:
        campos.append("TELEFONO = :4")
        valores.append(telefono)
    if direccion:
        campos.append("DIRECCION = :5")
        valores.append(direccion)

    if not campos:
        print("⚠️ No se proporcionaron campos para actualizar.")
        return

    sql += ", ".join(campos) + " WHERE ID = :id"
    valores.append(id_paciente)
    cursor.execute(sql, valores)
    conn.commit()
    print("✅ Paciente actualizado correctamente.")

def eliminar_paciente(id_paciente):
    sql = "DELETE FROM PACIENTES WHERE ID = :id"
    cursor.execute(sql, {"id": id_paciente})
    conn.commit()
    print("✅ Paciente eliminado correctamente.")

# =============================
# EJEMPLOS DE USO
# =============================

if __name__ == "__main__":
    # Crear pacientes
    crear_paciente("Juan Pérez", 30, "Masculino", "3001234567", "Calle 10 #20-30")
    crear_paciente("Ana Gómez", 25, "Femenino", "3109876543", "Carrera 15 #45-50")

    # Leer pacientes
    print("\n📋 Lista de pacientes:")
    leer_pacientes()

    # Actualizar paciente
    actualizar_paciente(1, telefono="3201112233", direccion="Nueva dirección 123")

    # Leer pacientes después de actualizar
    print("\n📋 Lista de pacientes actualizada:")
    leer_pacientes()

    # Eliminar paciente
    eliminar_paciente(2)

    # Leer pacientes después de eliminar
    print("\n📋 Lista final de pacientes:")
    leer_pacientes()

📌 4. Flujo del CRUD
Crear paciente → INSERT
Leer pacientes → SELECT
Actualizar paciente → UPDATE
Eliminar paciente → DELETE

🚀 Ejecución
Ejecuta el script en tu consola:
bash
python pacientes.py
Verás la secuencia de operaciones CRUD funcionando sobre la tabla PACIENTES en Oracle .
