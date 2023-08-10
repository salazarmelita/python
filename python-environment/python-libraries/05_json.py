import json

# Un diccionario de ejemplo
data = {
    "name": "Andrew",
    "age": 28,
    "city": "Santiago"
}
# Convertir el diccionario a una cadena JSON
# indent para una visualización más legible
cadena_json = json.dumps(data, indent=4)

#? Guardar la cadena JSON en un archivo
with open("data.json", "w") as archivo:
    archivo.write(cadena_json)
print("Datos guardados en data.json")

#? Cargar datos desde un archivo JSON
name_file_json = 'python-environment\python-libraries\config.configparser.json'
with open(name_file_json, "r") as archivo:
    datos_cargados = json.load(archivo)
print("Datos cargados desde datos.json:", datos_cargados)



#? Otra ejemplificación para obtener las variables de entorno
with open(name_file_json) as config_file:
    config_data = json.load(config_file)

db_host = config_data['Server']['hostname']
db_port = config_data['Server']['port']
db_username = config_data['User']['username']
db_password = config_data['User']['password']

print(f"Database Host: {db_host}")
print(f"Database Port: {db_port}")
print(f"Database Username: {db_username}")
print(f"Database Password: {db_password}")
