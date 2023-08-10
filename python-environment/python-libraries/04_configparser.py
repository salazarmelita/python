import json
import configparser

# Lectura el archivo JSON
with open('python-environment\workspace\salazarmelita-py.json') as json_file:
    config_data = json.load(json_file)

#? Crear un objeto ConfigParser
config_parser = configparser.ConfigParser()

# Agregar secciones y opciones basadas en los datos del JSON
for section, options in config_data.items():
    config_parser[section] = options

#? Escribir el nuevo archivo INI
with open('config.ini', 'w') as ini_file:
    config_parser.write(ini_file)
    print('Archivo .ini creado')