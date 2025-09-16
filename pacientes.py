import oracledb

#configura la conexion a oracle
conn = oracledb.connect(
    user="system",
    password="Tapiero123",
    dsn="localhost:1521/orcl"
)
cursor = conn.cursor

# =============================
# FUNCIONES CRUD
# =============================

def crear_paciente(nombre, edad, genero, telefono, direccion):
    sql = """INSERT INTO PACIENTES (NOMBRE, EDAD, GENERO, TELEFONO, DIRECCION)
            VALUES (:1, :2, :3, :4, :5)"""
    cursor.execute(sql, (nombre, edad, genero, telefono, direccion))
    conn.commit()
    print("✅ Paciente creado correctamente .")

def leer_pacientes():
    sql = "SELECT ID, NOMBRE, EDAD, GENERO, TELEFONO, DIRECCION, FECHA_REGISTRO FROM PACIENTES"
    cursor.execute(sql)
    pacientes = cursor.fetchall()
    for p in pacientes:
        print(p)

def actualizar_paciente(id_paciente, nombre=None, edad=None, genero=None, telefono=None, direccion=None):
    sql=" UPDATE PACIENTES SET "
    campos=[]
    valores=[]

    if nombre:
        campos.append("NOMBRE = :1 ")
        valores.append(nombre)
    if edad:
        campos.append("EDAD = :2 ")
        valores.append(edad)
    if genero:
        campos.append("GENERO = :3 ")
        valores.append(genero)
    if telefono:
        campos.append("TELEFONO = :4 ")
        valores.append(telefono)
    if direccion:
        campos.append("DIRECCION = :5 ")
        valores.append(direccion)
    
    if not campos:
        print("⚠️ No se proporcionaron campos para actualizar .")
        return
    
    sql += ", ".join(campos) + "WHERE ID = :id"
    valores.append(id_paciente)
    cursor.execute(sql, valores)
    conn.commit()
    print("✅ Paciente actualizado correctamente .")

def eliminar_paciente(id_paciente):
    sql = "DELETE FROM PACIENTES WHERE ID = :id"
    cursor.execute(sql, {"id": id_paciente})
    conn.commit()
    print("✅ Paciente eliminado correctamente .")

# =============================
# EJEMPLOS DE USO
# =============================

if __name__ == "__name__":
    #crear pacientes
    crear_paciente("juan perez", 40, "masculino", "3001234567", "Calle 10 #20-30")
    crear_paciente("ana gomez", 45, "femenino", "3109876543", "Carrera 15 #45-50")

    #leer pacientes
    print("\n📋 Lista de pacientes: ")
    leer_pacientes()

    #actualizar paciente
    actualizar_paciente(1, telefono="3201112233", direccion="Nueva dirección 123")

    #leer pacientes despues de actualizar
    print("\n📋 Lista de pacientes actualizada: ")
    leer_pacientes()    

    #eliminar paciente     
    eliminar_paciente(2)

    #leer pacientes despues de eliminar
    print("\n📋 Lista final de pacientes :")
    leer_pacientes()    
    


    
