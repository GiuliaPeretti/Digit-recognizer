import numpy as np 
import pandas as pd 

<<<<<<< Updated upstream
data_train = pd.read_csv('mnist_train.csv')
data_train = np.array(data_train)  
#np.random.shuffle(data)

#m -> numero di foto
#n -> numero di pixel +1
m_train, n_train = data_train.shape

data_train=data_train.T
y_train = data_train[0]
#x_train -> tutto senza le soluzioni
x_train = data_train[1:n_train]
x_train = x_train / 255.
_,m_train = x_train.shape



=======
>>>>>>> Stashed changes


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
    return A

def one_hot(Y):
<<<<<<< Updated upstream
    #crea una matrice composta solo da 0, di dimensioni 
    #righe: numero di foto
    #colone: risultato massimo ottenibile(9(+1 perchè c'e anche lo 0))
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    #per ogni riga della matriche nella colonna y (BO) e mettila a 1
=======
    #mx10
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
>>>>>>> Stashed changes
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y
  
def derivata_Relu(z):
    return (z>0)

<<<<<<< Updated upstream
def forward(w1, w2, b1, b2, x):
=======
def forward_prop(w1, w2, b1, b2, x):
>>>>>>> Stashed changes
    z1 = w1.dot(x) + b1
    a1=relu(z1)
    z2 = w2.dot(a1) + b2
    a2=softmax(z2)
    return(z1, a1, z2, a2)

<<<<<<< Updated upstream
def back(z1, a1, z2, a2, w2, x, y):
=======
def back_prop(z1, a1, z2, a2, w2, x, y, m):
    #dato che il risultato mi viene restituito in una matrice 10xm con valori da 0 a 1
    #in cui la posizione in cui si trova il valore più alto corrispone al numero riconosciuto
    #one_hot_y trasforma la soluzione nella stesso modo
>>>>>>> Stashed changes
    one_hot_y=one_hot(y)

    #errori per il secondo layer
    dz2 = a2 - one_hot_y
<<<<<<< Updated upstream

    dw2 = 1/m_train * dz2.dot(a1.T)

    db2 = 1/m_train * np.sum(dz2) #(dz2, 2)
    
=======
    dw2 = 1/m * dz2.dot(a1.T)
    db2 = 1/m * np.sum(dz2)

>>>>>>> Stashed changes
    #errori per il primo layer
    #prendo i valori dell'ultimo layer e devo "undo" l'applicazione dei weight 
    #poi devo disfare anche la funzione di attivazione
    dz1 = w2.T.dot(dz2) * derivata_Relu(z1)
    dw1 = 1/m * dz1.dot(x.T)
    db1 = 1/m * np.sum(dz1)
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
    return(np.sum(prediction == y)/y.size)
   
<<<<<<< Updated upstream
def train(x, y, iterations, alpha):
    w1, w2, b1, b2 = init_parameters()
    
    for i in range (iterations+1):
        z1, a1, z2, a2 = forward(w1, w2, b1, b2, x)
        dw1, db1, dw2, db2 = back(z1, a1, z2, a2, w2, x, y)
        w1, b1, w2, b2 = update_par(w1, b1, w2, b2, dw1, db1, dw2, db2, alpha)
=======
def train(iterations, lr):

    data_train = pd.read_csv('blackAndWhite.csv')
    data_train = np.array(data_train)  
    #np.random.shuffle(data)

    #m -> numero di foto
    #n -> numero di pixel +1
    m_train, n_train = data_train.shape
    data_train=data_train.T
    y_train = data_train[0]
    #x_train -> tutto senza le soluzioni
    x_train = data_train[1:]

    #rendere la riga di codice successiva eseguibile nel caso si stia allenando la rete sul dataset in scala di grigi
    #x_train = x_train / 255



    w1, w2, b1, b2 = init_parameters()
    
    for i in range (iterations+1):
        z1, a1, z2, a2 = forward_prop(w1, w2, b1, b2, x_train)
        dw1, db1, dw2, db2 = back_prop(z1, a1, z2, a2, w2, x_train, y_train, m_train)
        w1, b1, w2, b2 = update_par(w1, b1, w2, b2, dw1, db1, dw2, db2, lr)
>>>>>>> Stashed changes

        if (i%100==0):
            print("Iterazione: ",i)
            print("Accuratezza: ", get_accuracy(get_prediction(a2), y_train))

    return w1, b1, w2, b2
        

<<<<<<< Updated upstream
def guess(w1, b1, w2, b2, pixel, answer):
    pixel=pixel.reshape((-1,1))
=======
def guess(pixel):
    pixel = np.array(pixel)
    pixel=pixel.reshape((-1,1))
    w1, b1, w2, b2 = get_from_file()
>>>>>>> Stashed changes
    z1 = w1.dot(pixel) + b1
    a1=relu(z1)
    z2 = w2.dot(a1) + b2
    a2=softmax(z2)
    return(get_prediction(a2))

<<<<<<< Updated upstream


w1, b1, w2, b2 = train(x_train, y_train, 500, 0.122)


#TODO: finisci sta roba
data_test = pd.read_csv('mnist_test.csv')
data_train = np.array(data_train)  
#np.random.shuffle(data)

#m -> numero di foto
#n -> numero di pixel +1
m_train, n_train = data_train.shape

data_train=data_train.T
y_train = data_train[0]
#x_train -> tutto senza le soluzioni
x_train = data_train[1:n_train]
x_train = x_train / 255.
_,m_train = x_train.shape
print()
print("guess0")
guess(w1, b1, w2, b2, x_train.T[0], y_train[0])

print()
print("guess1")
guess(w1, b1, w2, b2, x_train.T[1], y_train[0])

print()
print("guess2")
guess(w1, b1, w2, b2, x_train.T[2], y_train[0])

print()
print("guess3")
guess(w1, b1, w2, b2, x_train.T[3], y_train[0])

print()
print("guess4")
guess(w1, b1, w2, b2, x_train.T[4], y_train[0])
# data_test = pd.read_csv('mnist_test.csv')
# data_test = np.array(data_test)  
# print(guess(data_test.T[0]))

#guess()
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

=======
def test():
    data_test = pd.read_csv('mnist_test.csv')
    data_test = np.array(data_test)  
    w1, b1, w2, b2 = get_from_file()

    data_test=data_test.T
    y_test = data_test[0]
    x_test = data_test[1:]
    x_test = x_test / 255.

    z1 = w1.dot(x_test) + b1
    a1=relu(z1)
    z2 = w2.dot(a1) + b2
    a2=softmax(z2) 
    print("Accuratezza: ", get_accuracy(get_prediction(a2), y_test))

def save_in_file(w1,b1,w2,b2):
    df = pd.DataFrame(w1)
    df.to_csv("W1.csv", index=False)
    df = pd.DataFrame(b1)
    df.to_csv("B1.csv", index=False)
    df = pd.DataFrame(w2)
    df.to_csv("W2.csv", index=False)
    df = pd.DataFrame(b2)
    df.to_csv("B2.csv", index=False)

def get_from_file():
    w1=pd.read_csv('MINST\W1.csv')
    w1 = np.array(w1)  

    b1=pd.read_csv('MINST\B1.csv')
    b1 = np.array(b1)  

    w2=pd.read_csv('MINST\W2.csv')
    w2 = np.array(w2)  

    b2=pd.read_csv('MINST\B2.csv')
    b2 = np.array(b2)  

    return(w1,b1,w2,b2)


# w1, b1, w2, b2 = train(500, 0.25)
# save_in_file(w1, b1, w2, b2)
>>>>>>> Stashed changes
