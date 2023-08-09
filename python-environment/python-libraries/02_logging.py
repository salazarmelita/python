import logging

logger = logging.getLogger(__name__)


#* Configuración de formato y salida
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#* Registro de mensajes
logger.debug("Este es un mensaje de depuración")
logger.info("Esta es una información relevante")
logger.warning("Esto es un aviso")
logger.error("Se ha producido un error")
logger.critical("Esto es un problema crítico")

#* Manejo de excepciones
def myFunction():
    try:
        # Código que puede generar excepciones
        return 
    except Exception as e:
        logger.exception("Se ha producido una excepción: %s", e)


#? Función que simula un error
def divide(a, b):
    try:
        result = a / b
        return result
    except Exception as e:
        logging.exception("Ha ocurrido una excepción: %s", e)
        return None

result = divide(200, 10)

if result is None:
    print("Error al realizar la división.")
else:
    print(f"El resultado de la división es: {result}")

print(divide(8,4))

#? Ejemplo uso de contexto
# Clase de contexto personalizado
class LoggingContext:
    def __init__(self, context_name):
        self.context_name = context_name

    def __enter__(self):
        logging.info(f'Entrando al contexto: {self.context_name}')
    
    def __exit__(self, exc_type, exc_value, traceback):
        logging.info(f'Saliendo del contexto: {self.context_name}')
        if exc_type is not None:
            logging.error(f'Se ha producido una excepción en el contexto: {exc_type}, {exc_value}')

# Uso del contexto personalizado
with LoggingContext('Operación importante'):
    logging.info('Realizando una operación dentro del contexto')
    result = 10 / 0  # Generar una excepción intencionalmente

logging.info('Operación fuera del contexto')