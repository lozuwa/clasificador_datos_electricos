import pandas as pd
import numpy as np


class NeuralNetwork(object):
    def __init__(self, dimensions, learning_rate):
        self.dimensions= dimensions
        self.parameters= {}
        self.learning_rate= learning_rate
        np.random.seed(5)
        for i in range(1,len(self.dimensions)):
            self.parameters['W'+str(i)]=np.random.randn(self.dimensions[i-1],self.dimensions[i])*np.sqrt(2/dimensions[i-1])
            self.parameters['b'+str(i)]=np.zeros((1,self.dimensions[i]))
    
    def sigmoid(self,Z):
        ''' 
        Función de activación sigmoide
        '''
        return 1 / (1 + np.exp(-Z))
    
    def forward_prop(self,X):
        ''' Propagración hacia adelante
        -------------------------------
        Arguments:
        X: Features con los cuales se entrena el modelo
        
        Returns:
        hidden_layer: resultado de la propagación hacia adelante de la capa oculta
        output_layer: resultado de la propagación hacia adelante del nodo de salida
        '''
        hidden_layer= self.sigmoid(np.dot(X,self.parameters['W1'])+self.parameters['b1'])
        output_layer= np.dot(hidden_layer, self.parameters['W2'])+self.parameters['b2']

        return hidden_layer, output_layer
    
    def backward_prop(self, X, y, output_layer, hidden_layer):
        """ Realiza la propagación hacia atrás
        ---------------------------
        Arguments:
        X: Features con los cuales se entrena el modelo
        y: target
        output_layer: resultado de la propagación hacia adelante del nodo de salida
        hidden_layer: resultado de la propagación hacia adelante de la capa oculta
        
        Returns:
        error: error de la predicción
        hidden_delta: error propagado a la capa oculta
        """
        error= y-output_layer
        hidden_error= np.dot(error,self.parameters['W2'].T)
        hidden_delta= hidden_error *(hidden_layer*(1-hidden_layer))

        return hidden_delta, error
    
    def update_weights(self, hidden_d, output_d, X, hidden_layer):
        """
        Actualiza los parámetros
        ----------------------------
        Arguments:
        hidden_d: error propagado a la capa oculta
        output_d: error de la predicción
        X: Features con los cuales se entrena el modelo
        hidden_layer: resultado de la propagación hacia adelante de la capa oculta"""
    
        n=X.shape[0]
        
        self.parameters['W1']+= self.learning_rate/n* np.dot(X.T,hidden_d)
        self.parameters['b1']+= self.learning_rate/n*np.sum(hidden_d,axis=0,keepdims=True)

        self.parameters['W2']+= self.learning_rate/n*np.dot(hidden_layer.T, output_d)
        self.parameters['b2']+= self.learning_rate/n*np.sum(output_d)
        
    def train(self,X,y):
        """
        Realiza el entrenamiento del modelo
        -------------------
        Arguments
        X: Features con los cuales se entrena el modelo
        y: target"""
        
        hidden_layer,output_layer=self.forward_prop(X)
        hidden_d, output_d= self.backward_prop(X, y, output_layer, hidden_layer)
        self.update_weights(hidden_d,output_d, X, hidden_layer )
        
    def test(self,X):
        """
        Predicción del modelo
        -----------------
        Arguments
        X:Features con los cuales se entrena el modelo """
        hidden_layer,output_layer=self.forward_prop(X)
        return output_layer

    @staticmethod
    def MSE(y=None, Y=None):
        """Calcula Mean Squared Error"""
        return 1/2*np.mean((y-Y)**2)



