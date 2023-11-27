# By: Dexne

# Analisis de prediccion filtrado en Zapopan
# El propósito del siguiente codigo es el de poder extraer todos los datos de las elecciones presidenciales de años anteriores y con ellos, tratar de hacer estimaciones y calculos acerca de los posibles resultados de las elecciones futuras.


# librerias necesarias
from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import scipy.stats
import scipy.stats as stats
import seaborn as sns
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa.stattools as sts
from IPython.display import Latex, Math, display
from prophet import Prophet
from scipy.stats.distributions import chi2
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

sns.set()


# Establecemos el tamanio predeterminado de las figuras que estaremos ploteando
plt.rcParams['figure.figsize'] = (16,8)

# Leemos nuestro archivo donde contenemos toda la información recopilada
df = pd.read_excel('content/TEST.xlsx')

# Podremos agregar un print en caso de querer visualizar la indfo
print(df.head())

print(df.tail())

filtro = df.loc[df['TpE'] == 'Municipes']

print(filtro)

filtro = df.loc[(df['TpE'] == 'Municipes') & (df['MUNICIPIO'] == "ZAPOPAN")]

print(filtro)

df = filtro

df.sort_values(by='YE') #Ordenamos el dataframe

df = df.sort_values(by='YE') #Ordenamos el dataframe

print(df.info())

print(df.isnull().sum())

print(df.head())

print(df.tail())

df.to_excel("content/serie_electio.xlsx")

# Serie de tiempo
stocks_df=pd.read_excel("content/serie_electio.xlsx")

print(stocks_df)

stocks_df['YE'] = stocks_df['YE'].replace(2006, "2006-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2009, "2009-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2012, "2012-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2015, "2015-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2018, "2018-12-31")
stocks_df['YE'] = stocks_df['YE'].replace(2021, "2021-12-31")

print(stocks_df)

print(stocks_df.info())

stocks_df['YE'] = pd.to_datetime(stocks_df['YE'])

print(stocks_df)

stocks_df.set_index("YE", inplace=True)

stocks_df_anual = stocks_df.resample('A').sum()

# Eliminar las filas donde hay puros ceros
stocks_df_anual = stocks_df_anual[(stocks_df_anual != 0).any(axis=1)]

print(stocks_df_anual)

stocks_df_anual.to_excel("content/anual_election.xlsx")
stocks_df_anual = pd.read_excel("content/anual_election.xlsx")
print(stocks_df_anual)

stocks_df = stocks_df_anual
print(stocks_df)

# Print out the number of stocks
print('Total Number of stocks : {}'.format(len(stocks_df.columns[1:])))

# Print the name of stocks
print('Stocks under consideration are:')

for i in stocks_df.columns[1:]:
    print(i)

print(stocks_df.info())

def show_plot(df, fig_title):
    df.plot(x = 'YE', figsize = (15,10), linewidth = 3, title = fig_title)
    plt.grid()
    plt.show()

# Mostrar los partidos
show_plot(stocks_df, 'Partidos')

def interactive_plot(df, title):
    fig = px.line(title = title)

    # Loop through each stock (while ignoring time columns with index 0)
    for i in df.columns[1:]:
        fig.add_scatter(x = df['YE'], y = df[i], name = i) # add a new Scatter trace

    fig.show()

# Plot interactive chart
interactive_plot(stocks_df, 'Partidos')

#Describe of the returns
stocks_df.describe()

# Daily Return Correlation
#cm = stocks_df.drop(columns = ['YE']).corr()

#plt.figure(figsize=(25, 25))
#ax = plt.subplot()
#sns.heatmap(cm, annot = True, ax = ax);}

numeric_df = stocks_df.select_dtypes(include=[np.number])

# Si hay columnas no numéricas o NaNs presentes, podrías limpiarlas o eliminarlas

# Calcular correlación
cm = numeric_df.corr()

plt.figure(figsize=(25, 25))
ax = plt.subplot()
sns.heatmap(cm, annot=True, ax=ax);
plt.show()

# Histogram of daily returns
# Stock returns are normally distributed with zero mean
stocks_df.hist(figsize=(20, 20), bins = 40);
plt.show()

# Imprimir las columnas presentes en el DataFrame
print(df.columns)

# Eliminar solo las columnas que existen en el DataFrame
columns_to_drop = ['YE', 'GroupVot', 'TpE', 'MUNICIPIO', 'MUN']  # Selecciona las columnas a eliminar
existing_columns_to_drop = [col for col in columns_to_drop if col in df.columns]  # Filtra las columnas existentes en el DataFrame
partidos_df = df.drop(existing_columns_to_drop, axis=1)  # Elimina las columnas existentes

# Convertir los datos a numéricos si no están en el formato correcto (esto es importante para calcular estadísticas)
partidos_df = partidos_df.apply(pd.to_numeric, errors='coerce')

# Calcular la media y la desviación estándar de los votos de los partidos
mean_votes = partidos_df.mean()
std_votes = partidos_df.std()

# Mostrar los resultados
print("Media de votos por partido:")
print(mean_votes)

print("\nDesviación estándar de votos por partido:")
print(std_votes)

# Hasta aqui vamos donde dice que instalemos prophet

df = pd.read_excel("content/anual_election.xlsx")

df = df.rename(columns={'YE': 'Año'})

df.set_index("Año", inplace=True)

print("Anio renombrado")
print(df)

df.info()

# AZUL - PAN
# AZUL = df['AZUL']
# AZUL.head()

# AZUL.plot(figsize=(20,5), title = "Votos por el partido AZUL")
# plt.show()

# scipy.stats.probplot(AZUL, plot =  plt)
# plt.title("QQ Plot", size = 24)
# plt.show()

# sts.adfuller(AZUL)
#no se rechaza la hipotesis nula, la serie no es estacionaria.

# dataframe = df['AZUL']
# dataframe.to_excel("content/AZUL.xlsx")
# dataframe = pd.read_excel("content/AZUL.xlsx")
# dataframe.head()
# dataframe.columns = ['ds', 'y']
# dataframe.head()

# p = Prophet(interval_width=0.95, daily_seasonality=True)
# model = p.fit(dataframe)
# future = p.make_future_dataframe(periods=3, freq='A')
# future.tail()
# forecast_prediction = p.predict(future)
# forecast_prediction[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

# plot1 = p.plot(forecast_prediction)
# plt.show()

# plot2 = p.plot_components(forecast_prediction)
# plt.show()

# Evitar repeticion y optmizacion de lineas de codigo
colores = ['AZUL', 'ROJO', 'AMARILLO', 'VERDE', 'TINTO', 'NARANJA', 'AZULVERDE', 'MAGENTA', 'MORADO', 'MEZCLA MAGENTA', 'FUTURO', 'ROJOVERDE', 'morado bajo', 'amarillo bajo', 
           'OTRO', 'NO CONTESTO', 'OTROB', 'MORADO.1', 'OTROC', 'ROSA']

for color in colores:
    # Obtener datos de la columna actual
    data = df[color]
    
    # Mostrar gráfico de la serie temporal
    data.plot(figsize=(20, 5), title=f"Votos por el partido {color}")
    plt.show()
    
    # Mostrar QQ Plot
    stats.probplot(data, plot=plt)
    plt.title("QQ Plot", size=24)
    plt.show()
    
    # Prueba de estacionariedad (Prueba ADF)
    adf_result = sts.adfuller(data)
    print(f"Resultados de la prueba ADF para {color}:")
    print(adf_result)
    print("\n")
    
    # Guardar datos en un archivo Excel
    data.to_excel(f"content/{color}.xlsx")
    df_color = pd.read_excel(f"content/{color}.xlsx")
    df_color.columns = ['ds', 'y']
    
    # Entrenar modelo Prophet
    p = Prophet(interval_width=0.95, daily_seasonality=True)
    model = p.fit(df_color)
    
    # Generar predicciones
    future = p.make_future_dataframe(periods=3, freq='A')
    forecast = p.predict(future)
    
    # Mostrar gráfico de predicción
    plot1 = p.plot(forecast)
    plt.show()
    
    # Mostrar componentes del modelo
    plot2 = p.plot_components(forecast)
    plt.show()
