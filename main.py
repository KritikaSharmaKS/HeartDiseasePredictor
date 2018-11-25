# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle

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
X_test = sc_X.transform(X_test)

# K-Nearest Neighbos (K-NN)
from sklearn.neighbors import KNeighborsClassifier
knn_classifier = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
knn_classifier.fit(X_train, Y_train)
print("{} NN Score: {:.2f}%".format(10, knn_classifier.score(X_test, Y_test)*100))

# Try to find best k value
"""scoreList = []
for i in range(1,20):
    knn_classifier2 = KNeighborsClassifier(n_neighbors = i)  # n_neighbors means k
    knn_classifier2.fit(X_train, Y_train)
    scoreList.append(knn_classifier2.score(X_test, Y_test))
    
plt.plot(range(1,20), scoreList)
plt.xticks(np.arange(1,20,1))
plt.xlabel("K value")
plt.ylabel("Score")
plt.show()


print("Maximum KNN Score is {:.2f}%".format((max(scoreList))*100))"""

# Predicting the test set result
Y_pred = knn_classifier.predict(X_test)

# Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)

# Visualising the training set results

# Visualising the test set results





