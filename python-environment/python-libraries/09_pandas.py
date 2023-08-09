# Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos. El nombre viene de “Panel data”.
import pandas as pd
import numpy as np

#todo: series y dataframes
#* Crear series
# índice automático
names = pd.Series(['Eliot','Erick','Martha','Genesis'])

# índice preestablecido
names_index1 = pd.Series(['Eliot','Erick','Martha','Genesis'],
          index=[1,7,10,30]
          )
# usando diccionarios
dict1 = {1:'Eliot',7:'Erick',10:'Martha',30:'Genesis'}
names_index2 = pd.Series(dict1)

print(names)
print(names_index1[0:2])
print(names_index2[10])


#* Crear DataFrames

# usando diccionarios
dict2 = {'Jugador':['Eliot','Erick','Martha','Genesis'], 'Altura':[170.2, 174.5, 168.0, 172.4], 'pets':['true', 'true', 'false', 'true']}
names_index3 = pd.DataFrame(dict2, index=[1,7,10,30])

print(names_index3)
print(names_index3.columns)
print(names_index3.index)


#todo: Lectura de archivos
# por default, el separador será la coma
# el header se puede definir por fila (númericamente), NONE establecerá un orden númerico como encabezado
# con la propiedad "name", podemos editar el encabezado
archive_csv = pd.read_csv(r'python-environment\python-libraries\files_for_examples\bestsellers-with-categories.csv', sep=',', header=0)
print(archive_csv)

# para llevarde una estructura json a una estructura pandas, usamos "typ='Series'"
archive_json = pd.read_json(r'python-environment\python-libraries\files_for_examples\HPCharactersDataRaw.json', typ='Series')
print(archive_json[0:4])

print(archive_csv[0:4])
print(archive_csv[['Name', 'Author']])



#todo: loc & iloc
# basados en labels, filtrado por filas y columnas
# filtra por posición, no por índice
print(archive_csv.loc[0:4, ['Name', 'Author']])
# puede afectar resultados intencionalmente
print(archive_csv.loc[:, ['Reviews']]*-1)
print(archive_csv.loc[:, ['Author']] == 'JJ Smith')

# filtrado pro el índice, pero es el de las columnas
print(archive_csv.iloc[:,0:2])
print(archive_csv.iloc[:2,2:])


#todo: Agregar o eliminar datos con pandas
#* retorna las dos primeras filas
#print(archive_csv.head(2)) 
#* sólo se elimina información de la salida
#archive_csv.drop('Genre', axis=1)
#* se elimina del dataframe
#archive_csv.drop('Genre', axis=1, inplace=True)
#* Otra forma no recomendada para eliminar: 
#del archive_csv['Genre']

#* Eliminar fila
#archive_csv.drop(0, axis=0)
#* Eliminar filas
#archive_csv.drop([0, 1, 2], axis=0)
#* Eliminar rango de filas
#archive_csv.drop([0,10], axis=0)

#* agregar columna, especificando un valor no numérico
#archive_csv['new column'] = np.nan
#* lista desde cero, llegando al número total de filas
#data = np.arange(0, archive_csv.shape[0])
#* agregar columna, especificando un total de valores igual al total de filas (asegurar esa condición)
#archive_csv['Range'] = data

#* agregar filas (anexar registros), duplicar registro:
#archive_csv.append(archive_csv)


#todo: Manejo de datos nulos
dict3 = {'Col1':[1, 2, 3, np.nan], 'Col2':[4, np.nan, 6, 7], 'Col3':['a', 'b', 'c', None]}
dataframe = pd.DataFrame(dict3) 
print(dataframe)
# verificar valores nulos (True o False)
print(dataframe.isnull())
# verificar valores nulos (0 o 1)
print(dataframe.isnull()*1)
# cambiar valor de elemento nulo
print(dataframe.fillna('missing'))
# cambiar valores por la media
# print(dataframe.fillna(dataframe.mean()))
# crea valores asumiendo cuales deberían seguir
print(dataframe.interpolate())
# eliminar valores nulos
print(dataframe.dropna())


#todo: Filtrado por condiciones
# filtro para múmeros
greater_than_2016 = archive_csv['Year'] > 2016
print(greater_than_2016)

# filtro por palabra
genre_fiction = archive_csv['Genre'] == 'Fiction'
print(genre_fiction)

# combinación de filtros
filter_combination = archive_csv[greater_than_2016 & genre_fiction]
print(filter_combination)


#todo: Funciones principales de pandas
# muestra los primeros registros
print(archive_csv.head(4))
# muestra los últimos registros
print(archive_csv.tail(4))
# señala detalles de las columnas
print(archive_csv.info())
# entrega datos estadísticos de las columnas númericas
print(archive_csv.describe())
# indica cuanta memoria estoy usando en mi dataframe
print(archive_csv.memory_usage(deep=True))
# indica cuanta memoria estoy usando en mi dataframe
print(archive_csv['Author'].value_counts())
# elimina columnas duplicadas, se puede elegir cual mantener
print(archive_csv.drop_duplicates(keep='last'))
# ordena los valores de manera descendente por columna 'Year'
print(archive_csv.sort_values('Year', ascending=False))


#todo: Groupby, agrupamiento o funciones de agregación
# verificar cuantos registros hay por autor
print(archive_csv.groupby('Author').count())
print(archive_csv.groupby('Author').sum())
print(archive_csv.groupby('Author').min())
print(archive_csv.groupby('Author').max())
#print(archive_csv.groupby('Author').mean()) #! esta función me genera problema

# "Author" es palabra clave, se transforma en el índice de mi columna al usar groupby, podemos usar loc
print(archive_csv.groupby('Author').sum().loc['William Davis'])
# Para regresar a "Author" al resto de títulos:
print(archive_csv.groupby("Author").sum().reset_index())

#agrupamiento por determinadas funciones de agregación
print(archive_csv.groupby("Author").agg(['min', 'max']))
#agrupamiento por determinadas funciones de agregación, especificando
print(archive_csv.groupby("Author").agg({'Reviews':['min', 'max'], 'User Rating':'sum'}))
# múltiples combinaciones agrupando datos
print(archive_csv.groupby(["Author", "Year"]).count())