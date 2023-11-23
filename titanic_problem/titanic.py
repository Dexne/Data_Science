# Titanic problem
# by: Dexne

# Liberias necesarias
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importamos el conujunto de datos para comenzar a trabajar en el
train_data = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv")
test_data =pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_test.csv")
test_survived_data =pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/gender_submission.csv")
test_data["Survived"] = test_survived_data["Survived"]

total_data = pd.concat([train_data, test_data]).reset_index(inplace=False)
total_data.drop(columns=["index"], inplace=True)
total_data.head() # Mostramos las primeras 5 filas

# Habilitamos para mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Mostramos los resultados
# print(total_data.head())

# Obtener las dimensiones
total_data.shape

# Obtener informacion sobre los tipos de datos y valores no nulos
total_data.info()

"""
Hasta el momento podemos decir lo siguiente:
    836 filas ( personas ) y 12 columnas donde encontramos la clase a predecir (Survived)
    Cabin solo tiene 295 instancias con valores, por lo cual podemos intuir que tendremos mas de 1000 valores nulos o que desconocemos
    Tenemos 7 caracteristicas numericas 5 logicas 
        -> [ float64(2), int64(5) ], [ object(5) ]
"""

# Eliminamos duplicados

# Eliminamos PassengerId ya que podría estar mal generado
total_data.drop("PassengerId", axis=1).duplicated().sum()

# En caso de encontrar duplicidades ejecutamos
total_data = total_data.drop_duplicates( subset= total_data.columns.difference(['PassengerId']))
print( total_data.shape )
total_data.head() # Agregamos un print en caso de querer visualizar


if total_data.duplicated().sum():
    total_data = total_data.drop_duplicates()
print( total_data.shape )
total_data.head()

# Eliminar datos "Despreciables" cosas que el modelo no usara
total_data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace= True)
total_data.head()

# Analisis de variable invariantes - Categoria o numerica ???
fig, axis = plt.subplots( 2, 3, figsize = ( 10, 7) )

# Creamos histograma multiple
sns.histplot(ax = axis[0,0], data = total_data, x = "Survived").set_xlim(-0.1,1.1)
sns.histplot(ax = axis[0,1], data = total_data, x = "Sex").set(ylabel = None)
sns.histplot(ax = axis[0,2], data = total_data, x = "Pclass").set(ylabel = None)
sns.histplot(ax = axis[1,0], data = total_data, x = "Embarked")
sns.histplot(ax = axis[1,1], data = total_data, x = "SibSp").set(ylabel = None)
sns.histplot(ax = axis[1,2], data = total_data, x = "Parch").set(ylabel = None)

plt.tight_layout()

# Mostramos resultados
plt.show()

"""
¿Que sabemos hasta el momento?

Murieron mas personas que las que sobrevivieron
La poblacion de hombres en el titanic era superior a la de las mujeres
Habia notoriamente mas personas de 3ra clase que de las demas
Mas tres cuatras partes de los pasajeros abordaron en Southampton
La mayoria de los pasajeros viajaron solos
"""

fig, axis = plt.subplots(2, 2, figsize = (10, 7), gridspec_kw={'height_ratios': [6, 1]})

# Crear una figura múltiple con histogramas y diagramas de caja
sns.histplot(ax = axis[0, 0], data = total_data, x = "Fare").set(xlabel = None)
sns.boxplot(ax = axis[1, 0], data = total_data, x = "Fare")
sns.histplot(ax = axis[0, 1], data = total_data, x = "Age").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[1, 1], data = total_data, x = "Age")

# Ajustar el layout
plt.tight_layout()

# Mostrar el plot
plt.show()

"""
¿Qué podemos decir?
La media es inferior a la moda
"""

# Analisis numerico-numerico
fig, axis = plt.subplots( 2,2, figsize = (10,7) )

# Creamos unos diagramas de dispersion multiple
sns.regplot( ax = axis[ 0,0 ], data = total_data, x= "Fare", y= "Survived")
sns.heatmap( total_data[["Survived", "Fare"]].corr(), annot= True, fmt=".2f", ax=axis[1,0], cbar = False)
sns.regplot(ax = axis[0,1], data = total_data, x= "Age", y="Survived").set(ylabel=None)
sns.heatmap(total_data[["Survived", "Age"]].corr(), annot=True,fmt = ".2f",ax = axis[1,1])

plt.tight_layout()
plt.show()

"""
Existe relacion aunque no muy fuerte entre el precio del billete y la supervivencia del pasajero. Algunos pasajeros con un importe bajo de billete tivbieron menos probabilidad de supervivencia frente a los que adquirieron un billete con un precio mayor.
También existe una relacion lineal negativa entre la edad y la variable objetivo. Esto hace sentido ya que los niños tenian preferencia al momento de abordar los botes
"""

# Determinar el grado de afinidad o correlacion
fig, axis = plt.subplots(2,1, figsize = (5,7) )

# Diagrama de dispercion simple
sns.regplot(ax = axis[0], data = total_data, x = "Age", y = "Fare")
sns.heatmap(total_data[["Fare", "Age"]].corr(), annot=True, fmt = ".2f", ax = axis[1])

plt.tight_layout()
plt.show()

"""
poco que decir, lo mas destacable es que la edad no importaba mucho en relacion con el precio del billete. Ademas de que podemos apreciar como la mayor parte de los datos se concentra en la parte de abajo, esto una vez más hace sentido ya que en su mayoria los pasajeros eran de tercera clase
"""

# Analisis categorico Survived - Sex, Pclass, Embarkedm SibSp and Parch
fig, axis = plt.subplots(2,3,figsize = (15, 5))

sns.countplot(ax = axis[0,0], data = total_data, x = "Sex", hue="Survived")
sns.countplot(ax = axis[0,1], data = total_data, x = "Pclass", hue="Survived").set(ylabel = None)
sns.countplot(ax = axis[0,2], data = total_data, x = "Embarked", hue="Survived").set(ylabel = None)
sns.countplot(ax = axis[1,0], data = total_data, x = "SibSp", hue="Survived")
sns.countplot(ax = axis[1,1], data = total_data, x = "Parch", hue="Survived").set(ylabel = None)

plt.tight_layout()
fig.delaxes(axis[1,2])
plt.show()

"""
Con mayor proporcion sobrevivieron las mujeres frente a los hombres.
Tiene sentido ya que se les estaban dando prioridad a mujeres y niños.
Las personas que viajaron solas tuvieron mas problemas para sobrevivir drente a las que viajaron acompañadas.
Aquellos que viajaron en una mejor clase en el titanic tuvieron una mayor probabilidad de supervivencia.
"""

# Analisis multivariable
fig, axis = plt.subplots( figsize = (10,5), ncols= 2)

sns.barplot(ax = axis[0], data=total_data, x="Sex", y="Survived", hue= "Pclass")
sns.barplot(ax = axis[1], data= total_data, x= "Embarked", y="Survived", hue="Pclass").set(ylabel = None)

plt.tight_layout()
plt.show()

"""
Podemos observar que claramente, independientemente del puerto de embarque las mujeres tuvieron mas posibilidades de supervivencia independientemente de la clase en la que viajaron, reforzando nuestro punto anterior.
Las personas que viajaron en clases mas altas sobrevivieron mas que aquellos que no lo hicieron.
"""

# Analisis de correlaciones
total_data["Sex_n"] = pd.factorize(total_data["Sex"])[0]
total_data["Embarked_n"] = pd.factorize(total_data["Embarked"])[0]

fig, axis = plt.subplots(figsize = (10, 6))

sns.heatmap(total_data[["Sex_n", "Pclass", "Embarked_n", "SibSp", "Parch", "Survived"]].corr(), annot = True, fmt = ".2f")

plt.tight_layout()
plt.show()

"""
El analisis refleja una fuerte relacion entre el sexo del pasajero y su supervivicia
Se aprecia una relación entre el número de acompañantes de los pasajeros (variables SibSp y Parh).
"""

# Analisis Numerico-Categorico completo
fig, axis = plt.subplots(figsize = (10, 7))

sns.heatmap(total_data[["Age", "Fare", "Sex_n", "Pclass", "Embarked_n", "SibSp", "Parch", "Survived"]].corr(), annot = True, fmt = ".2f")

plt.tight_layout()
plt.show()

"""
Existe una relacion entre la clase Pclass y la edad del pasajero Age fuertemente negativa ya que las personas que viajaban en primera clase eran personas de edad avanzada en su mayoria y entre Pclass y tarifa, algo que de nuevo tiene sentido.
"""

fig, axis = plt.subplots(figsize = (10, 5), ncols=2)

sns.regplot(ax=axis[0], data = total_data, x = "Age", y = "Pclass")
sns.regplot(ax=axis[1], data=total_data, x = "Fare", y = "Pclass").set(ylabel = None, ylim = (0.9, 3.1))

plt.tight_layout()
plt.show()

"""
Aqui podemos obervar de una manera más clara y consisa que conforme la edad aumenta, el dinero crece (porque personas de edad avanzada eran personas que tenian boletos de primera clase) 
"""

# Dibujamos el pairplot
#sns.pairplot(data = total_data)
#plt.show() # Forzar matplotlib

pairplot = sns.pairplot(data = total_data)
pairplot.savefig('pairplot.png') # Guardamos el grafico como una imagen

# Analisis Descriptivo
total_data.describe()

# También podemos dibujar sus diagramas para hacerlo mas visual
fig, axis = plt.subplots(3,3, figsize = (15,10))

sns.boxplot(ax = axis[0,0], data = total_data, y = "Survived")
sns.boxplot(ax = axis[0,1], data = total_data, y = "Pclass")
sns.boxplot(ax = axis[0,2], data = total_data, y = "Age")
sns.boxplot(ax = axis[1,0], data = total_data, y = "SibSp")
sns.boxplot(ax = axis[1,1], data = total_data, y = "Parch")
sns.boxplot(ax = axis[1,2], data = total_data, y = "Fare")
sns.boxplot(ax = axis[2,0], data = total_data, y = "Sex_n")
sns.boxplot(ax = axis[2,1], data = total_data, y = "Embarked_n")

plt.tight_layout()
plt.show()

fare_stats = total_data["Fare"].describe()
fare_stats

fare_iqr = fare_stats["75%"] - fare_stats["25%"]
upper_limit = fare_stats["75%"] + 1.5 * fare_iqr
lower_limit = fare_stats["25%"] - 1.5 * fare_iqr

print(f"Los límites superior e inferior para la búsqueda de outliers son {round(upper_limit, 2)} y {round(lower_limit, 2)}, con un rango intercuartílico de {round(fare_iqr, 2)}")

# según los precios que vimos en el diagrama de caja, los valores más extremos están por encima de 300. Veamos cuántos valores representan ese valor extremo de 512

print(total_data[total_data["Fare"] > 300])

"""
Quiza pueda haber un impacto real entre el precio del boleto y la supervivencia, por lo cual lo dejaremos como un valor atipico
"""

# Analisis de valores faltantes