# Introducción al Data Science - Problema del titanic
### By. Dexne

**¿En qué consiste el problema del ticanic?**
El "Problema del Titanic" es un desafío común en el campo de la ciencia de datos y el aprendizaje automático. Se basa en un conjunto de datos que contiene información sobre los pasajeros a bordo del famoso transatlántico RMS Titanic, que se hundió trágicamente en su viaje inaugural en abril de 1912.

El objetivo principal de este problema es predecir si un pasajero sobrevivió o no al desastre del Titanic. A partir de características como edad, sexo, clase socioeconómica (Pclass), número de hermanos/cónyuges a bordo (SibSp), número de padres/hijos a bordo (Parch), entre otros, se intenta construir un modelo predictivo que pueda determinar con precisión si un pasajero sobrevivió al naufragio o no.

**¿Cómo fue realizado?**
Para la resolución de este problema de tomaron datos "sucios" acerca de lo que se conoce acerca de esta tragedia, estos fueron tratados mediante técnicas de analisis de datos con ayuda del lenguaje de programación Python, apoyandonos de librerías utiles para la manipulación de información y datos como Matplotlib, Pandas, Seaborn y algunos modulos de sklearn.

**¿Qué información logramos obtener de los datos?**
De todo el personal que iba a bordo del barco, más de 800 personas resultaron sin vida, solamente poco más de 500 personas lograron sobrevivir.

Se estima que la población de los hombres a bordo superaba por mas de 300 a la de las mujeres, siendo estas alrededor de poco menos de 500.

También podemos apreciar que la mayor parte de los pasajeros viajó en 3ra clase, representando estos en igual cantidad que la suma de la 1ra y 2da clase.

También podemos observar que más de la mitad de las personas abordaron desde S = Southampton, seguido por C = Cherbourg y finalmente Q = Queenstown.

Y otro dato importante que podemos destacar es que la mayoria de los pasajeros viajaron solos.

![Figura 1](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_1.png)

De la siguiente imagen podemos decir que una población significativa de los pasajeros pago una tarifa baja, esto hace sentido ya que, como lo vimos antes, la mayor parte de los pasajeros viajó en 3ra clase y también tiene relación con las edades calculadas, sabemos gracias a analisis posteriores que por lo general, la población de edad más avanzada era la que viajaba en 3ra clase, o sea, una porción muy pequeña.

![Figura 2](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_2.png)

Podemos apreciar que existe una relación directa entre el precio del billete y la supervivencia del pasajero.

Además también podemos apreciar que existe una relación lineal negativa entre la edad y la supervivencia, nuevamente hace sentido ya que los niños y las mujeres tenian prioridad al momento de subir a los botes salvavidas.

![figura 3](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_3.png)

En la siguiente imagen podemos sacar conclusiones de que la edad no es un factor que tenga una relación muy grande en los precios de los billetes.

![figura 4](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_4.png)

En la imagen de a continuación si que tenemos mucha información importante que logramos obtener como:
De las personas que NO lograron sobrevivir podemos calcular que más de 600 de ellos fueron hombres, mientras que mujeres solo representan poco más de 100. Por otro lado, de la población que SI logró sobrevivir podemos ver como en su mayoria se trata de mujeres al poco menos de 400, mientras que hombres apenas y llegaron a los 100. Nuevamente esto tiene sentido debido a la prioridad que se tenia en los botes salvavidas.

Sorpresivamente de las personas que sobrevivieron estan casi empatadas las personas que pagaron un boleto de 1ra y 3ra clase, quedando un poco por debajo los de 2da clase, sin embargo, si lo comparamos con las personas que no lograron sobrevivir, podemos apreciar como las personas de 3ra clase superan por mucho incluso sumando las de 2da y 3ra clase. Nuevamente esto hace sentido ya que era mucho más númerosa la población de personas de 3ra clase.

Así mismo también podemos afirmar que las personas que abordaron desde S = Southampton, representan la población que más y al mismo tiempo la que menos logro salvarse.

Finalmente y reafirmando mi punto anterior, podemos ver como las personas que viajaron solos tuvieron mayor exito en la supervivencia.

![figura 5](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_5.png)

Hablando un poco de esta población que afortunadamente logró sobrevivir, podemos decir lo siguiente:

De los hombres, casi el doble pagaron por un boleto más caro, siendo el de primera clase, mientras que los demás eran casi en cantidades iguales de 2da y 3ra clase. Por el otro lado, la población de sobrevivientes mujeres fueron casi iguales de 1ra y 2da clase, estas ultimas solo un poco menor que las de primera y las de 3ra clase, aunque un poco menos que las anteriores, siguieron representando una cantidad superior a la de la suma de todos los hombres incluso.

De estas personas, la mayoría de ellas (de primera clase) embarcaron desde Queenstown y Cherbourg y, solo un poco menor desde Southampton.

![Figura 6](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_6.png)

Haciendo un analisis de correlaciones podemos apreciar que existe una relación directa enyre el sexo del pasajero y su supervivencia, como hemos visto anteriormente. Además, se aprecia una relación entre el número de acompañantes de los mismos.

![Figura 7](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_7.png)

Se observa una asociación inversa entre la clase socioeconómica y la edad de los pasajeros. En general, aquellos que viajaban en primera clase tienden a ser personas de mayor edad en comparación con los pasajeros de segunda y tercera clase. Esta relación negativa sugiere que, en promedio, los pasajeros de mayor edad eran más propensos a viajar en primera clase.

![Figura 8](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_8.png)

Para reafirmar el punto anterior podemos basarnos en el siguiente gráfico. Podemos observar como conforme la edad incrementa, el precio del billete aumenta, confirmando que las personas de edad avanzada tendian a ser las que viajaban en primera clase. Así mismo, conforme el precio disminuye, la cantidad de boletos aumenta (Ya que había mas personas con billete de 3ra clase).

![Figura 9](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Figure_9.png)

**Datos limpios para entrenamiento**

Después de varios procesos logramos extraer dos archivos .csv bastante descentes y limpios, podemos encontrarlos aquí:

[clean_titanic_test.csv](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/workspaces/machine-learning-content/assets/clean_titanic_test.csv)

[clean_titanic_train.csv](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/workspaces/machine-learning-content/assets/clean_titanic_train.csv)

Aquí una pequeña representación de la neurona logistica usada:

![Neurona logistica](https://github.com/Dexne/Data_Science/blob/main/titanic_problem/resultados/Neurona_Logistica.png)


## Conclusión

**Relación entre características y supervivencia:** Se evidencia una fuerte relación entre ciertas características (como sexo, clase socioeconómica y acompañantes) y las posibilidades de supervivencia de los pasajeros. Por ejemplo, las mujeres y los pasajeros de primera clase tenían mayores probabilidades de sobrevivir, mientras que los hombres y aquellos en tercera clase tenían tasas de supervivencia más bajas.

**Diferencias en edad y tarifa según clase socioeconómica:** Se observa una asociación inversa entre la edad y la clase socioeconómica, indicando que los pasajeros de mayor edad tendían a viajar en primera clase. Además, se aprecia que los boletos de primera clase tenían tarifas más altas en comparación con las de segunda y tercera clase.

**Efecto del género y acompañantes en la supervivencia:** La proporción de supervivientes varía significativamente según el género y el número de acompañantes. Las mujeres y aquellos que viajaban con un número limitado de acompañantes tuvieron tasas de supervivencia más altas.

**Relación entre edad y tarifa pagada:** Aunque no se encontró una relación muy significativa entre la edad de los pasajeros y el precio de los boletos, se observó que las personas de mayor edad tendían a pagar tarifas más altas, lo que coincidía con su preferencia por la primera clase.

En conclusión, el análisis detallado del conjunto de datos del Titanic revela patrones claros sobre qué características influían en las posibilidades de supervivencia de los pasajeros. Los hallazgos resaltan la importancia del sexo, la clase socioeconómica y la presencia de acompañantes como factores clave para determinar las probabilidades de supervivencia en el desastre del Titanic. Este análisis proporciona valiosa información sobre las dinámicas sociales y demográficas presentes en aquel trágico evento, además de servir como un ejercicio fundamental en ciencia de datos y análisis exploratorio de datos.
