import pandas as pd
import numpy as np

archive_csv = pd.read_csv(r'python-environment\python-libraries\files_for_examples\bestsellers-with-categories.csv', sep=',', header=0)
dataframe1 = archive_csv.head(4)

def two_times(value):
    return value*2

# ejemplificando funcionamiento
apply_method = dataframe1['User Rating'].apply(two_times)
print(apply_method)

archive_csv['Rating_2'] = archive_csv['User Rating'].apply(two_times)
print(archive_csv)

# creando lambda functions
archive_csv.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1)
