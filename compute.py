# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle

def computeResult(X_test_new):
    # Import the dataset
    dataset = pd.read_csv('heart.csv')
    #dataset = shuffle(dataset)
    X = dataset.iloc[:, :-1].values #matrix of independent variables
    Y = dataset.iloc[:, 13].values #matrix of dependent variables
    
    # Taking care of missing data
    from sklearn.preprocessing import Imputer
    imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 0)
    imputer.fit(X)
    X = imputer.transform(X)
    
    # Splitting the dataset into training and test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    
    # K-Nearest Neighbos (K-NN)
    from sklearn.neighbors import KNeighborsClassifier
    knn_classifier = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
    knn_classifier.fit(X_train, Y_train)
    # Predicting the test set result
    Y_pred = knn_classifier.predict(X_test_new)
    return Y_pred[0]

X_test_new = np.array([[41,0,1,130,204,0,0,172,0,1.4,2,0,2]])
print(computeResult(X_test_new))