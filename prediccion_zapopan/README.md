# Predicción elecciones presidenciales

### BY: Dexne


El data science juega un papel fundamental en el análisis de elecciones presidenciales al permitir el procesamiento y la interpretación de grandes conjuntos de datos para identificar patrones, tendencias y factores predictivos.

Es importante destacar que, aunque el data science puede proporcionar información valiosa y predicciones, los resultados electorales dependen de numerosos factores imprevistos, como eventos de última hora, cambios en las percepciones de los votantes y factores externos. Por lo tanto, las predicciones basadas en el análisis de datos deben considerarse como estimaciones probabilísticas y no como resultados definitivos.

En esta ocasión estamos trabajando con una serie de datos que simulan los votos que han tenido los diversos partidos políticos a lo largo de los años, con ellos, pretendemos lograr hacer estimaciones para poder obtener la mayor la cantidad de información posible, datos importantes como lo pueden ser los momentos en los cuales los partidos han llegado a tener su mayor auge, cuando comenzó a desender, en qúe lugares se ve más reflejado el apoyo, entre muchas otras cuestiones que, en algún momento, para ciertas campañas, pudieran resultar en una gran ayuda para el sector político.

**¿Qué información logramos conseguir?**

Para comenzar con la sintesis de los resultados debemos de entrar en contexto, partimos de una tabla en la cual contenemos datos como: Nombre de partidos (en nuestro caso por cuestiones de prácticidad y demostración se han cambiado los nombres de los partidos reales por colores), años en los cuales se dieron elecciones de candidatura, municipios donde se registraron los votos, etc.

Comenzando por el primer gráfico, podemos apreciar una imagen que nos hace referencia a unas gráficas de lineas, dentro de la cual podemos descatar lo siguiente:

Durante el año 2019 fue el momento en el cual el partido NARANJA tuvo su más grande auge e influencia, obteniendo el valor más grande y por mucho respecto a la competencia con más de 250 mil votos.

Por parte de los demás contendientes podemos apreciar como en los años 2013 los partidos ROJO y AZUL estaban casi empatados en cuanto al número de simpatizantes con los que estos contaban, luego de esos años su popularidad se vio afectada callendo drásticamente sus números.

El años 2016 fue un año clave y el descisivo, si suponemos que los años de cambio de presidente concuerdan con lo del mundo real, el partido NARANJA fue el ganador por casí más de 60 mil votos superando a los partidos ROJO y AZUL, esto graciasa a la fuerza y popularidad que iba creciendo desde los años 2010-2013.

![Partidos]()

Con ayuda del siguiente mapa de calor podemos darnos una idea de si existen o no existen relaciones entre las variables de los colores.

Si observamos en la parte inferior derecha podemos apreciar que existen unos patrones de correlación  similares entre los partidos ROSA, OTROC, MORADO.1 y OTROB por lo cual podemos pensar que existe una correlación positiva fuerte.

Por el otro lado, si nos vamos a la parte inferior izquierda y la superior derecha podemos apreciar algo similar, gracias al mapa de calor podemos ver que existe una correlación negativa entre los partidos AZUL, ROJO, AMARILLO, VERDE y TINTO, de manera que si una de estas variables aumenta las demás decrementan.

Por lo demás, podemos decir que son datos independientes entre si y no existe una relación tan fuerte, esto no quiere decir que sean datos inservibles, pero para este analisis se dejarán un poco de lado.

![heatmap]()

Para corroborar aún más lo antes dicho podemos apoyarnos del gráfico siguiente, con el cual podemos apreciar de una forma más visual el número de los votos de todos los partidos en comparación entre ellos mismos. Recordando un poco a lo que vimos en los gráficos primeros pudimios observar como el partido NARANJA fue el que más votos obtuvo y por mucho, esto mismo podemos apreciarlo en este histograma.

![Histograma_diario]()

# Partido AZUL

Ahora pasemos al análisis detallado de los datos de cada partido individual

Hablemos de cómo le fue al partido AZUL, el cual gracias al siguiente gráfico podemos observar como en el año 2012 tuvo su mayor cantidad de votos, los cuales fueron alrededor de 180 mil, después de ese año su popularidad al igual que sus votos fueron disminuyendo, llegando a un total de 60 mil por el año 2020, una perdida de casi dos terceras partes.

![Votos AZUL]()

En los gráficos, los puntos negros representan los datos observados y la línea azul con el área sombreada representa el pronóstico. La línea azul muestra la tendencia central del pronóstico y el área sombreada alrededor de la línea azul representa el intervalo de confianza del pronóstico.

Se muestra una tendencia descendente desde 2010 hasta 2018, seguida de una ligera tendencia ascendente desde 2018 hasta 2024. Esto sugiere que la variable que se está pronosticando disminuyó durante un período y luego comenzó a aumentar.

![Forecast AZUL]()
![Forecast AZUL 2]()


Lo siguiente es más de los mismo pero para cada partido en especifico, sin embargo omitiré hacer una descripción especifica para cada partido y condensaré todo en una conclusión final.

# Partido ROJO

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()


# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()

# Partido 

![]()
![]()
![]()
![]()


# Partido 

![]()
![]()
![]()
![]()
