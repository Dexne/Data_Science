# neurona para la prediccion - Problema del titanic
# Para esta implementación se hace uso de una neurona logistica

# Agregamos las liberias necesarias para los calculos y el preprocesamiento
import numpy as np
from sklearn import preprocessing


# Definicion de la clase donde establecemos las entredas de nuestro csv y ela taza de aprendizaje
class LogisticNeuron:
    def __init__(self, n_inputs, learning_rate=0.1) -> None:
        # Inicializamos con valores random en un incio
        self.w = -1 + 2 * np.random.rand(n_inputs)
        self.b = -1 + 2 * np.random.rand()
        self.eta = learning_rate

    # Funcion de la predicción, aquí es donde se resulve la ecuación que nos dice
    #          1
    #    ------------
    #            -z
    #       1 + e

    def predict_proba(self, X):
        Z = np.dot(self.w, X) + self.b # Calculamos el producto punto
        return (1 / (1 + np.exp(-Z)))

    def predict(self, X, umbral=0.5) -> int:
        Z = np.dot(self.w, X) + self.b
        Y_est = (1 / (1 + np.exp(-Z)))
        return 1.0 * (Y_est > umbral)

    def fit(self, X, Y, epochs=500):
        p = X.shape[1]
        for _ in range(epochs):
            Y_est = self.predict_proba(X)
            self.w += (self.eta/p) * np.dot((Y - Y_est), X.T).ravel()
            self.b += (self.eta/p) * np.sum(Y - Y_est)

if __name__=="__main__":
    # dependiendo de los resultados que obtengamos podemos ajustar los valores de las epocas y la taza de aprendizaje
    epochs, learning_rate, I = 1000, 0.015, 5

    # Datos para el entrenamiento
    X = np.genfromtxt("workspaces/machine-learning-content/assets/clean_titanic_train.csv", delimiter=',', skip_header=1, usecols= [i for i in range(I)]).T # transpuesta de la matriz
    
    # resultados
    Y = np.genfromtxt("workspaces/machine-learning-content/assets/clean_titanic_train.csv", delimiter=',', skip_header=1, usecols= [I]).T

    for i in range(I):
        # Escalamos las x 
        X[i, :] = preprocessing.minmax_scale(X[i, :])

    # generamos la neurona
    neuron = LogisticNeuron(X.shape[0], learning_rate)

    print('W:\t', neuron.w )
    neuron.fit(X, Y, epochs=epochs)
    print('W:\t', neuron.w )

    predic = neuron.predict(X)
    good = 0
    for i in range(X.shape[1]):
        print("x [ "+ str(i) + "] =>" + str(predic[i])) # Mostrar Vive o muere
        if ( predic[i] == Y[i] ):
            good += 1
    
    print("Accurancy:\t", good/X.shape[1]) # Mostrar el porcentaje de precisión