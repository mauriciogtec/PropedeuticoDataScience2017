#######################################################################
### Parte 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image







#####################################################################
## Ejercicio 1

# Importar imagen


imagen = Image.open('C:/Users/Data Mining/Documents/ITAM/Propedeutico/Alumnos/PropedeuticoDataScience2017/Alumnos/Leonardo_Marin/black_and_white.jpg')
imagen_gris = imagen.convert('LA')   ## Convertir a escala de grises


## Convertir la imagen a una matriz

imagen_mat = np.array(list(imagen_gris.getdata(band=0)), float)
imagen_mat.shape = (imagen_gris.size[1], imagen_gris.size[0])
imagen_mat = np.matrix(imagen_mat)

plt.figure(figsize=(9, 6))
plt.imshow(imagen_mat, cmap='gray')


## Desomposición singular

U, sigma, V = np.linalg.svd(imagen_mat)



## Probar la visualización con los primeris n vectores

# n= 1
j = 1
matriz_equivalente = np.matrix(U[:, :j]) * np.diag(sigma[:j]) * np.matrix(V[:j, :])
plt.figure(figsize=(9, 6))
plt.imshow(matriz_equivalente, cmap='gray')


# n = 5
j = 5
matriz_equivalente = np.matrix(U[:, :j]) * np.diag(sigma[:j]) * np.matrix(V[:j, :])
plt.figure(figsize=(9, 6))
plt.imshow(matriz_equivalente, cmap='gray')

# n = 25
j = 25
matriz_equivalente = np.matrix(U[:, :j]) * np.diag(sigma[:j]) * np.matrix(V[:j, :])
plt.figure(figsize=(9, 6))
plt.imshow(matriz_equivalente, cmap='gray')

# n = 50
j = 50
matriz_equivalente = np.matrix(U[:, :j]) * np.diag(sigma[:j]) * np.matrix(V[:j, :])
plt.figure(figsize=(9, 6))
plt.imshow(matriz_equivalente, cmap='gray')


## Podemos ver como se puede reconstruir la imagen sin utilizar toda la información de la matriz original,











#####################################################################
## Ejercicio 2

A = np.array([[1,0],[1,2]])
A


def pseudoinversa(A):
    U,s,V=np.linalg.svd(A)
    D1 = np.dot(V,(np.diag(1/s)))
    peudoinversa = np.dot(D1,U.T)
    return peudoinversa

B = pseudoinversa(A)
B

def sistema_ecuaciones(A,b):
    #Resuelve un sistema de ecuaciones, A es la matriz con los coeficentes de las ecuaciones, b es el vector de  re sesultados
    x = np.dot(pseudoinversa(A),b.T)
    return(x)    


A = np.array([[1,0],[1,2]])
A
A.shape

b = np.array([[5,3]])
b
b.shape


## Probar la Función
sistema_ecuaciones(A,b)


## 





