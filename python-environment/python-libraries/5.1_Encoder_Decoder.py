
import json

class Persona:
    def __init__(self, nombre, edad, rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut

# Personalizar el codificador JSON
class PersonaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Persona):
            # Omitir el número de seguridad social en la codificación
            return {"nombre": obj.nombre, "edad": obj.edad}
        return super().default(obj)

# Personalizar el decodificador JSON
def persona_decoder(diccionario):
    if "nombre" in diccionario and "edad" in diccionario:
        return Persona(diccionario["nombre"], diccionario["edad"], None)
    return diccionario

persona = Persona("Andres", 28, "18942018-8")


# Codificación personalizada
cadena_json = json.dumps(persona, cls=PersonaEncoder, indent=4)
print("Codificacion personalizada:")
print(cadena_json)

# Decodificación personalizada
cadena_json = '{"nombre": "Maria", "edad": 50, "rut": "12405235-1"}'
objeto_decodificado = json.loads(cadena_json, object_hook=persona_decoder)
print("\nDecodificacion personalizada:")
print(objeto_decodificado.__dict__)