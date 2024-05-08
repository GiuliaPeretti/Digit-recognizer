import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt
#np.set_printoptions(threshold=np.inf)

data_train = pd.read_csv('mnist_train.csv')
data_train = np.array(data_train)  
#np.random.shuffle(data)

#m -> numero di foto
#n -> numero di pixel +1
m_train, n_train = data_train.shape

data_train=data_train.T
y_train = data_train[0]
x_train = data_train[1:n_train]
x_train = x_train / 255.
_,m_train = x_train.shape

# print(m_train)
# print(n_train)
# print(y_train)
# print()
# print(x_train)




def init_parameters():
    w1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10,1) - 0.5
    w2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10,1) - 0.5
    return(w1,w2,b1,b2)
    

def relu(z):
    #np.maximum prende 2 array e li compara, per ogni elemento dei due array li compara e insersce il più alto in un nuovo array
    #in questo caso compariamo z con un array di solui 0, se il numero è minoore di 0 diventerà 0 altrimenti non cambierà
    return (np.maximum(z,0))

def softmax(z):
    A = np.exp(z) /  sum(np.exp(z))
    # c=0
    # for i in  np.exp(z):
    #     p=np.isnan(i)
    #     for j in p:
    #         if j==True:
    #             c=c+1

    # print(c)
    return A

def one_hot(Y):
    #crea una matrice composta solo da 0, di dimensioni 
    #righe: numero di foto
    #colone: risultato massimo ottenibile(9(+1 perchè c'e anche lo 0))
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    #per ogni riga della matriche nella colonna y (BO) e mettila a 1
    one_hot_Y[np.arange(Y.size), Y] = 1
    #ogni colonna deve essere un esempio invece che ogni riga
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

    
def derivata_Relu(z):
    return (z>0)

def forward(w1, w2, b1, b2, x):
    z1 = w1.dot(x) + b1
    a1=relu(z1)
    z2 = w2.dot(a1) + b2
    a2=softmax(z2)
    # c=0
    # for i in  a2:
    #     p=np.isnan(i)
    #     for j in p:
    #         if j==True:
    #             c=c+1

    # print(c)
    # print("i: ",i)
    # print("j: ",j)
    return(z1, a1, z2, a2)

def back(z1, a1, z2, a2, w2, x, y):
    one_hot_y=one_hot(y)

    #errori per il secondo layer
    dz2 = a2 - one_hot_y

    dw2 = 1/m_train * dz2.dot(a1.T)
    #print(np.isnan( dz2.dot(a1.T)))

    #p=np.isnan(a1)

    db2 = 1/m_train * np.sum(dz2) #(dz2, 2)
    
    #errori per il primo layer
    #prendo i valori dell'ultimo layer e devo"undo" l'applicazione dei weight 
    #poi devo disfare anche la funzione di attivazione
    dz1 = w2.T.dot(dz2) * derivata_Relu(z1)
    dw1 = 1/m_train * dz1.dot(x.T)
    db1 = 1/m_train * np.sum(dz1)
    return(dw1, db1, dw2, db2)


def update_par(w1, b1, w2, b2, dw1, db1, dw2, db2, alpha):
    w1 = w1 - alpha*dw1
    b1 = b1 - alpha*db1
    w2 = w2 - alpha*dw2
    b2 = b2 - alpha*db2
    return (w1, b1, w2, b2)

def get_prediction(a2):
    return(np.argmax(a2, 0))

def get_accuracy(prediction, y):
    print(prediction, y)
    return(np.sum(prediction == y)/y.size)
   
def non_ho_caputo(x, y, iterations, alpha):
    w1, w2, b1, b2 = init_parameters()
    
    for i in range (iterations+1):

        z1, a1, z2, a2 = forward(w1, w2, b1, b2, x)
        dw1, db1, dw2, db2 = back(z1, a1, z2, a2, w2, x, y)
        w1, b1, w2, b2 = update_par(w1, b1, w2, b2, dw1, db1, dw2, db2, alpha)

        if (i%100==0):
            print("Iterazione: ",i)
            print("Accuratezza: ", get_accuracy(get_prediction(a2), y))
        
            
    return(w1,b1,w2,b2)


w1, b1, w2, b2 = non_ho_caputo(x_train, y_train, 4000, 0.122)
# y=[4,5,1,2]
# print(y)
# y=np.array(y)
# print(one_hot(y))

# p=np.isnan(data_train)
# for i in data_train:
#     p=np.isnan(i)
#     for j in p:
#         if j==True:
#             print("nan")
#             break;
#     if j==True:
#         break;



#softmax genera dei nan
#sum(np.exp(z)) mi sa che da qualche inf

# a = np.random.rand(5, 5) - 0.5
# print(a)
# print(softmax(a))

