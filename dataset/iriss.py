import pandas as pd
import numpy as np
import seaborn
import sklearn

iris =pd.read_csv('Iris_csv.csv')
print(iris.head(150))#menampilkan isi dari dataset
print (iris.describe())