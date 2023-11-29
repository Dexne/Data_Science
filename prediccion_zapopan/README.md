# Predicción elecciones presidenciales

### By: Dexne


El data science juega un papel fundamental en el análisis de elecciones presidenciales al permitir el procesamiento y la interpretación de grandes conjuntos de datos para identificar patrones, tendencias y factores predictivos.

Es importante destacar que, aunque el data science puede proporcionar información valiosa y predicciones, los resultados electorales dependen de numerosos factores imprevistos, como eventos de última hora, cambios en las percepciones de los votantes y factores externos. Por lo tanto, las predicciones basadas en el análisis de datos deben considerarse como estimaciones probabilísticas y no como resultados definitivos.

En esta ocasión estamos trabajando con una serie de datos que simulan los votos que han tenido los diversos partidos políticos a lo largo de los años, con ellos, pretendemos lograr hacer estimaciones para poder obtener la mayor la cantidad de información posible, datos importantes como lo pueden ser los momentos en los cuales los partidos han llegado a tener su mayor auge, cuando comenzó a desender, en qúe lugares se ve más reflejado el apoyo, entre muchas otras cuestiones que, en algún momento, para ciertas campañas, pudieran resultar en una gran ayuda para el sector político.

**¿Qué información logramos conseguir?**

Para comenzar con la sintesis de los resultados debemos de entrar en contexto, partimos de una tabla en la cual contenemos datos como: Nombre de partidos (en nuestro caso por cuestiones de prácticidad y demostración se han cambiado los nombres de los partidos reales por colores), años en los cuales se dieron elecciones de candidatura, municipios donde se registraron los votos, etc.

Comenzando por el primer gráfico, podemos apreciar una imagen que nos hace referencia a unas gráficas de lineas, dentro de la cual podemos descatar lo siguiente:

Durante el año 2019 fue el momento en el cual el partido NARANJA tuvo su más grande auge e influencia, obteniendo el valor más grande y por mucho respecto a la competencia con más de 250 mil votos.

Por parte de los demás contendientes podemos apreciar como en los años 2013 los partidos ROJO y AZUL estaban casi empatados en cuanto al número de simpatizantes con los que estos contaban, luego de esos años su popularidad se vio afectada callendo drásticamente sus números.

El años 2016 fue un año clave y el descisivo, si suponemos que los años de cambio de presidente concuerdan con lo del mundo real, el partido NARANJA fue el ganador por casí más de 60 mil votos superando a los partidos ROJO y AZUL, esto graciasa a la fuerza y popularidad que iba creciendo desde los años 2010-2013.

![Partidos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Partidos.png)

Con ayuda del siguiente mapa de calor podemos darnos una idea de si existen o no existen relaciones entre las variables de los colores.

Si observamos en la parte inferior derecha podemos apreciar que existen unos patrones de correlación  similares entre los partidos ROSA, OTROC, MORADO.1 y OTROB por lo cual podemos pensar que existe una correlación positiva fuerte.

Por el otro lado, si nos vamos a la parte inferior izquierda y la superior derecha podemos apreciar algo similar, gracias al mapa de calor podemos ver que existe una correlación negativa entre los partidos AZUL, ROJO, AMARILLO, VERDE y TINTO, de manera que si una de estas variables aumenta las demás decrementan.

Por lo demás, podemos decir que son datos independientes entre si y no existe una relación tan fuerte, esto no quiere decir que sean datos inservibles, pero para este analisis se dejarán un poco de lado.

![heatmap](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Headmap_partidos.png)

Para corroborar aún más lo antes dicho podemos apoyarnos del gráfico siguiente, con el cual podemos apreciar de una forma más visual el número de los votos de todos los partidos en comparación entre ellos mismos. Recordando un poco a lo que vimos en los gráficos primeros pudimios observar como el partido NARANJA fue el que más votos obtuvo y por mucho, esto mismo podemos apreciarlo en este histograma.

![Histograma_diario](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Histograma_diario.png)

# Partido AZUL

Ahora pasemos al análisis detallado de los datos de cada partido individual

Hablemos de cómo le fue al partido AZUL, el cual gracias al siguiente gráfico podemos observar como en el año 2012 tuvo su mayor cantidad de votos, los cuales fueron alrededor de 180 mil, después de ese año su popularidad al igual que sus votos fueron disminuyendo, llegando a un total de 60 mil por el año 2020, una perdida de casi dos terceras partes.

![Votos AZUL](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_AZUL.png)

En los gráficos, los puntos negros representan los datos observados y la línea azul con el área sombreada representa el pronóstico. La línea azul muestra la tendencia central del pronóstico y el área sombreada alrededor de la línea azul representa el intervalo de confianza del pronóstico.

Se muestra una tendencia descendente desde 2010 hasta 2018, seguida de una ligera tendencia ascendente desde 2018 hasta 2024. Esto sugiere que la variable que se está pronosticando disminuyó durante un período y luego comenzó a aumentar.

![Forecast AZUL](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_AZUL.png)
![Forecast AZUL 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_AZUL.png)


Lo siguiente es más de los mismo pero para cada partido en especifico, sin embargo omitiré hacer una descripción especifica para cada partido y condensaré todo en una conclusión final.

# Partido ROJO

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_ROJO.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_ROJO.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_ROJO.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_ROJO.png)

# Partido AMARILLO

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_AMARILLO.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_AMARILLO.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_AMARILLO.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_AMARILLO.png)

# Partido VERDE

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_VERDE.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_VERDE.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_VERDE.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_VERDE.png)

# Partido TINTO

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_TINTO.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_TINTO.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_TINTO.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_TINTO.png)

# Partido NARANJA

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_NARANJA.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_NARANJA.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_NARANJA.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_NARANJA.png)

# Partido AZULVERDE

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_AZULVERDE.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_AZULVERDE.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_AZULVERDE.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_AZULVERDE.png)

# Partido MAGENTA

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_MAGENTA.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_MAGENTA.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_MAGENTA.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_MAGENTA.png)

# Partido MORADO

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_MORADO.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_MORADO.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_MORADO.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_MORADO.png)


# Partido FUTURO

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_FUTURO.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_FUTURO.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_FUTURO.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_FUTURO.png)

# Partido ROJOVERDE

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_ROJOVERDE.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_ROJOVERDE.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_ROJOVERDE.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_ROJOVERDE.png)

# Partido morado bajo

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_moradobajo.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_moradobajo.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_moradobajo.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_moradobajo.png)

# Partido amarillo bajo

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_amarillobajo.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_amarillobajo.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_amarillobajo.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_amarillobajo.png)

# Partido OTRO

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_OTRO.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_OTRO.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_OTRO.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_OTRO.png)

# Partido NO CONTESTÓ

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_NoContesto.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_NoContesto.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_NoContesto.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_NoContesto.png)

# Partido OTROB

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_OTROB.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_OTROB.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_OTROB.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_OTROB.png)


# Partido MORADO.1

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_MORADO.1.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_MORADO.1.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_MORADO.1.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_MORADO.1.png)

# Partido OTROC

![votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_OTROC.png)
![qq](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_OTROC.png)
![forecast](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_OTROC.png)
![forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_OTROC.png)

# Partido ROSA

![Votos](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Votos_ROSA.png)
![QQ](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/QQ_ROSA.png)
![Forecast 1](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_ROSA.png)
![Forecast 2](https://github.com/Dexne/Data_Science/blob/main/prediccion_zapopan/assets/Forecast_prediction_components_ROSA.png)

## Conclusiones


**Análisis exploratorio de datos:** Se pueden realizar análisis descriptivos iniciales para comprender la estructura de la tabla de votos. Esto incluiría la identificación de variables clave, como el número de votos por candidato, tendencias de participación electoral a lo largo del tiempo, distribución geográfica de los votos, entre otros.

**Visualización de datos:** Gráficos y visualizaciones pueden ayudar a presentar patrones, relaciones y tendencias en los datos de manera clara y comprensible. Gráficos de barras, mapas de calor, gráficos de líneas temporales y mapas geoespaciales podrían utilizarse para mostrar la distribución de votos por región, cambios en la participación a lo largo de los años, entre otros aspectos relevantes.

**Detección de anomalías o irregularidades:** El Data Science puede ayudar a identificar patrones inusuales en los datos que podrían indicar irregularidades electorales, como votos anómalos, discrepancias significativas entre regiones o cambios repentinos en los patrones de votación.

**Segmentación y análisis demográfico:** No fue el caso pero la segmentación de votantes según características demográficas (edad, género, nivel educativo, etc.) puede proporcionar información valiosa sobre las preferencias electorales y patrones de participación, lo que ayuda a los candidatos a entender mejor a su electorado.

**Optimización de campañas electorales:** Utilizando técnicas de análisis predictivo, se pueden identificar estrategias más efectivas para las campañas electorales, como la asignación óptima de recursos, la identificación de temas relevantes para los votantes o la determinación de áreas clave para concentrar esfuerzos de campaña.

En resumen, el Data Science aplicado al registro de votos en elecciones presenciales proporciona herramientas poderosas para comprender patrones electorales, predecir tendencias, identificar áreas de mejora y tomar decisiones más informadas en el ámbito político. Además, puede contribuir significativamente a mejorar la transparencia y la integridad de los procesos electorales al identificar posibles irregularidades.

Finalmente para concluir este analisis podemos decir que, en base a los datos recabados que conforman los resultados de las elecciones de los ultimos años podemos decir que el partido ganador de las siguientes elecciones será el NARANJA ya que, como pudimos observar, la cantidad de los votos que recibia incrementaba con cada elecciones, a pesar de que tuvo un descenso en los últimos años, sigue siendo superior a la competencia. También podemos apreciar como su predicción nos dice que superará los 300,000 votos para el 2025 y su popularidad seguirá creciendo de manera lineal para esos años.
