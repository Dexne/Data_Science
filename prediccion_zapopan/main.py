# Analisis de prediccion filtrado en Zapopan
# El propósito del siguiente codigo es el de poder extraer todos los datos de las elecciones presidenciales de años anteriores y con ellos, tratar de hacer estimaciones y calculos acerca de los posibles resultados de las elecciones futuras.


from math import sqrt

# librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa.stattools as sts
from IPython.display import Latex, Math, display
from scipy.stats.distributions import chi2
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose

sns.set()

# Establecemos el tamanio predeterminado de las figuras que estaremos ploteando
plt.rcParams['figure.figsize'] = (16,8)

# Leemos nuestro archivo donde contenemos toda la información recopilada
df = pd.read_excel('content/TEST.xlsx')

# Podremos agregar un print en caso de querer visualizar la indfo
df.head()

df.tail()

filtro = df.loc[ df['TpE'] == 'Municipes' ]
print( filtro )

filtro = df.loc[(df['TpE'] == 'Municipes') & (df['MUNICIPIO'] == "ZAPOPAN")]
print( filtro )

df = filtro
df.sort_values( by='YE' )# Ordenamos el dataframe

df = df.sort_values( by='YE') # Ordenamos

df.info()

df.isnull().sum()

df.head()

df.tail()

df.to_excel("serie.xlsx")

stocks_df = pd.read_excel("content/serie_electio.xlsx")

print(stocks_df)

stocks_df['YE'] = stocks_df['YE'].replace(2006, "2006-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2009, "2009-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2012, "2012-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2015, "2015-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2018, "2018-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2021, "2021-12-31")

print(stocks_df)

stocks_df.info()

stocks_df['YE'] = pd.to_datetime(stocks_df['YE'])

print(stocks_df)

stocks_df.set_index("YE", inplace=True)
stocks_df_anual = stocks_df.resample('A').sum()
print(stocks_df_anual)

stocks_df_anual.to_excel("anual_election.xlsx")
stocks_df_anual = pd.read_excel("/content/anual_election.xlsx")
print(stocks_df_anual)

stocks_df = stocks_df_anual
print(stocks_df)

# Print out the number of stocks
print('Total Number of stocks : {}'.format(len(stocks_df.columns[1:])))

# Print the name of stocks
print('Stocks under consideration are:')

for i in stocks_df.columns[1:]:
  print(i)

stocks_df.info()

def show_plot(df, fig_title):
  df.plot(x = 'YE', figsize = (15,10), linewidth = 3, title = fig_title)
  plt.grid()
  plt.show()

show_plot(stocks_df, 'Partidos')

