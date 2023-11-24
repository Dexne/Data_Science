# Analisis de prediccion filtrado en Zapopan
# El propósito del siguiente codigo es el de poder extraer todos los datos de las elecciones presidenciales de años anteriores y con ellos, tratar de hacer estimaciones y calculos acerca de los posibles resultados de las elecciones futuras.


# librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error

# Establecemos el tamanio predeterminado de las figuras que estaremos ploteando
plt.rcParams['figure.figsize'] = (16,8)

# Leemos nuestro archivo donde contenemos toda la información recopilada
df = pd.read_excel('content/TEST.xlsx')

# Podremos agregar un print en caso de querer visualizar la indfo
print(df.head())
