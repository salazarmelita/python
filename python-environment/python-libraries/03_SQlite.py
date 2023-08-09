import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('example.db')

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos en la tabla
usuarios = [
    (1, 'Juan', 25),
    (2, 'María', 30),
    (3, 'Carlos', 28)
]
cursor.executemany('INSERT INTO usuarios VALUES (?, ?, ?)', usuarios)

# Confirmar los cambios
conn.commit()

# Realizar una consulta
cursor.execute('SELECT * FROM usuarios')
rows = cursor.fetchall()

# Imprimir los resultados
for row in rows:
    print(f'ID: {row[0]}, Nombre: {row[1]}, Edad: {row[2]}')

# Cerrar la conexión
conn.close()