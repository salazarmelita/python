import pandas as pd
import numpy as np

archive_csv = pd.read_csv(r'python-environment\python-libraries\files_for_examples\bestsellers-with-categories.csv', sep=',', header=0)


#todo: Pivot
#? Pivot, básicamente, transforma los valores de determinadas columnas o filas en los índices de un nuevo DataFrame, y la intersección de estos es el valor resultante.
print(archive_csv.head(5))
# los valores de Author pasan a formar el índice por fila y los valores de Genre pasan a formar parte de los índices por columna, y el User Rating se mantiene como valor.
print(archive_csv.pivot_table(index='Author', columns='Genre', values='User Rating'))
# tenemos por cada género, la suma a lo largo de los años
print(archive_csv.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum'))


#todo: Melt
#? El método melt toma las columnas del DataFrame y las pasa a filas, con dos nuevas columnas para especificar la antigua columna y el valor que traía.
# usaremos el siguiente apartado de la tabla
dataframe0 = archive_csv[['Name','Genre']].head(5)
# Ahora cada resultado de las dos columnas pasa a una fila de este modo a tipo llave:valor.
dataframe1 = archive_csv.head(5)

print(dataframe0.melt())
print(dataframe1.melt(id_vars='Year', value_vars='Genre'))