import numpy as np 
import pandas as pd 

data_train = pd.read_csv('mnist_train.csv')
data_train = np.array(data_train) 

for i in data_train:
    for j in i:
        if(j>=127):
            j=1;
        else:
            j=0;

data_train = pd.DataFrame(data_train)
data_train = pd.DataFrame.to_csv('blackAndWhite.csv')