import pandas as pd
import numpy as np

#todo: Merge

df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
 'B':['B0', 'B1', 'B2', 'B3'],
 'C':['C0', 'C1', 'C2', 'C3'],
 'D':['D0', 'D1', 'D2', 'D3'],
})

df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
 'B':['B4', 'B5', 'B6', 'B7'],
 'C':['C4', 'C5', 'C6', 'C7'],
 'D':['D4', 'D5', 'D6', 'D7'],
})


# los índices heredan el anterior, a menos que agreguemos "ignore_index"
print(pd.concat([df1, df2], ignore_index=True))
# por default concat se ejecuta con axis=0 (orientado a las filas), a menos que se específique
print(pd.concat([df1, df2], axis=1))


#todo: Concat

izq = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
'A':['A0', 'A1', 'A2', 'A3'],
 'B':['B0', 'B1', 'B2', 'B3'],
})
der = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
 'C':['C0', 'C1', 'C2', 'C3'],
 'D':['D0', 'D1', 'D2', 'D3'],
})
# caso con la misma key nombrada
print(izq.merge(der, on='key'))


izq2 = pd.DataFrame({'key_1': ['k0', 'k1', 'k2', 'k3'],
'A':['A0', 'A1', 'A2', 'A3'],
 'B':['B0', 'B1', 'B2', 'B3'],
})
der2 = pd.DataFrame({'key_2': ['k0', 'k1', 'k2', 'k3'],
 'C':['C0', 'C1', 'C2', 'C3'],
 'D':['D0', 'D1', 'D2', 'D3'],
})
# caso con distintas keys
print(izq2.merge(der2, left_on='key_1', right_on='key_2'))


# si existen valores nulos podemos utilizar "how", para forzar los datos en la tabla creada, priorizando left o rigth
# por defecto how será "how=inner" y omitirá valores coincidencias nulas

#todo: Join
izq3 = pd.DataFrame({'A':['A0', 'A1', 'A2'],
 'B':['B0', 'B1', 'B2']}, index=['k0', 'k1', 'k2'])

der3 = pd.DataFrame({'C':['C0', 'C1', 'C2'],
 'D':['D0', 'D1', 'D2'],}, index=['k0', 'k2', 'k3'])

print(izq3.join(der3, how='outer'))