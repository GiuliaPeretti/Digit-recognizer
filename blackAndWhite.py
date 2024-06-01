import numpy as np 
import pandas as pd 

data_train = pd.read_csv('mnist_train.csv')
data_train = np.array(data_train) 

rows,cols=data_train.shape
print(data_train)
print(rows,cols)

for i in range(0, rows):
    for j in range (0, cols):
        if(j==0):
            continue
        if(data_train[i][j]>=127 and j!=0):
            data_train[i][j]=int(1)
        else:
            data_train[i][j]=int(0)

data_train = pd.DataFrame(data_train)
data_train.to_csv('blackAndWhite.csv', header=False, index=False)
print("fine")
