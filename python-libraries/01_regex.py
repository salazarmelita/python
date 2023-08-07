# https://docs.python.org/es/3/library/re.html#module-re
import re

# analisis de expresiones regulares, se agrega modificador 'r'
regex = r"\d"

# texto a analizar
text = "La lluvia en Sevilla es una maravilla y la cama de España es la caña"
paragraph = """Tengo 2  COCHES: EL 1° aunque EXTRAÑA
... costó 12432 $"""


#* devuelve la primera coincidencia como un objeto de la clase 'match'
search = re.search(regex, text)
# search_group = re.search(regex,text).group()
# un tercer parametro es 'flags'

#* retorna todas las coincidencias no superpuestas
findall = re.findall(regex, text) 

#* busca una coincidencia perfecta
match = re.match(regex, text)

#* modifica elementos del string
sub = re.sub(regex, '*', paragraph)

#print(search_group)
print(search)
print(findall)
print(match)
print(sub)

#? Flags útiles
# flags = re.MULTILINE      #*--> para tratar cada linea independientemente
# flags = re.IGNORECASE     #*--> para no diferencias entre minúsculas y mayúsculas

#? Flags múltiples
#flags = re.MULTILINE | flags = re.IGNORECASE


#? Ejemplos retornados con re.findall()
# "ca[mñ]a"     #* cualquiera de los caracteres [mñ] sirve
# "ca[^mñ]a"    #* los caracteres siguientes al circunflejo se negarán
# "[a-z]"       #* entrega las letras minúsculas por separado del rango especificado
# "ña$"         #* indica como debe acabar el item del string evaluado
# "[a-z]+"      #* entrega las letras minúsculas consecutivas del rango especificado

# "\d"          #* representa los números entre 0-9
# "\d{4,6}"     #* entrega números que tengan entre 4 a 6 digitos consecutivos
# "\d{4,6}\b"   #* entrega números que terminen con 4 a 6 digitos consecutivos
# "\b\d{4,6}\b" #* entrega números que terminen e inicien con 4 a 6 digitos exactos consecutivos
# "^1\d+"       #* si se incia con el circunflejo, es requisito que el string evaluado incie con el carácter entregado
# "\d+"         #* representa los números consecutivos que contengan 0 a 9
# "\D"          #* retorna todo lo que no sea números, incluidos espacios y saltos de línea

# "w+"          #* devuelve las palabras o números que pueden formar parte de un idioma
# "\W+"         #* devuelve todo lo que no forme parte de un idioma: espacios, saltos de línea, moneda, etc.

# "s+"          #* devuelve spacios y saltos de línea
# "\S+"         #* devuelve todo lo que no sea un espacio Unicode

# "colou+r"          #* la 'u' debe coincidir 1 ó más veces
# "colou*r           #* la 'u' debe coindidir 0 ó más veces
# "colou?r           #* la 'u' debe coindidir 0 ó 1 vez
# "colou{3}r         #* la 'u' debe coindidir y devolverse 3 veces

#? Caso, obtener números de string
stringExample = "   cama 135 - 230 x 220 cm     45,99 $ En stock"

searchCaseOne = re.search(r"(\d+) x (\d+)", stringExample).group(1) # 230
searchCaseTwo = re.search(r"(\d+) x (\d+)", stringExample).group(2) # 220

findallCaseZero = re.findall(r"(\d+) x (\d+)", stringExample)       # [('230','220')]
findallCaseOne = re.findall(r"(\d+) x (\d+)", stringExample)[0]     # ('230','220')
findallCaseTwo = re.findall(r"(\d+) x (\d+)", stringExample)[0][0]  # 230
findallCaseThree = re.findall(r"(\d+) x (\d+)", stringExample)[0][1]  # 220

print(searchCaseOne)
print(searchCaseTwo)

print(findallCaseZero)
print(findallCaseOne)
print(findallCaseTwo)
print(findallCaseThree)