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
    
