import numpy as np

lista = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
lista_np = np.array(lista)
print(lista_np)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_np = np.array(matriz)
print(matriz_np)
# buscando elemento --> [fila, columna]
print(matriz_np[0,2])
print(matriz_np[0])

# El indexado nos permite acceder a los elementos de los array y matrices
# Los elementos se empiezan a contar desde 0.

#todo: Slices
print(lista_np[1:5])    # toma los valores entre los índices 1 y 5
print(lista_np[2:])     # toma todo desde el índice 2
print(lista_np[:6])     # toma todo hasta el índice 6
print(lista_np[:])      # muestra todo
print(lista_np[::3])    # muestra todo de 3 en 3
print(lista_np[-1:])    # ingresa desde el final

print(matriz_np[1:,0:2]) # separación entre nivel de filas y columnas

#todo: Tipos de datos
#? Los arrays de NumPy solo pueden contener un tipo de dato, ya que esto es lo que le confiere las ventajas de la optimización de memoria.
print(lista_np.dtype)

# Si queremos usar otro tipo de dato, lo podemos definir en la declaración del array.
lista2_np = np.array(lista, dtype='float64')
print(lista2_np)
print(lista2_np.dtype)

# Si ya posee el tipo definido se usará ".astype()" para convertir el tipo de dato
lista2_np = lista2_np.astype(np.int64)
print(lista2_np)
print(lista2_np.dtype)

# podemos convertir los datos en tipo string.
lista2_np = lista2_np.astype(np.string_)
print(lista2_np)
print(lista2_np.dtype)

# se puede pasar de string a número, s-i un elemento no es de tipo número, el método falla.
lista2_np = lista2_np.astype(np.int32)
print(lista2_np)
print(lista2_np.dtype)

# se puede cambiar a tipo booleano recordando que los números diferentes de 0 se convierten en True.
lista2_np = lista2_np.astype(np.bool_)
print(lista2_np)
print(lista2_np.dtype)