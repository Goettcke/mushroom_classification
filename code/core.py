import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets 
import numpy as np
from sklearn.preprocessing import CategoricalEncoder



#Read the data and remove labels
mushroom_data = pd.read_csv("../data/agaricus-lepiota.data", header = None)
print(mushroom_data.keys())
target = mushroom_data[[19]]
mushroom_data = mushroom_data.drop([19],axis = 1) # axis 1 for dropping columns 
fixed_mushrooms = CategoricalEncoder(mushroom_data)
print(type(x))
#Make Naive Bayes Classifier
nb = GaussianNB() 
#y_pred = nb.fit(mushroom_data.as_matrix(),target.as_matrix()).predict(mushroom_data)