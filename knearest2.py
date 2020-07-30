import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from csv import reader

iris = pd.read_csv("iris.csv")
print(iris.head())


#Drop id column

X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
#Split arrays or matrices into random train and test subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
'''
print("\n70% train data:")
print(X_train)
print(y_train)
print("\n30% test data:")
print(X_test)
print(y_test)
'''
#Create KNN Classifier
#Number of neighbors to use by default for kneighbors queries.
knn = KNeighborsClassifier(n_neighbors=5)
#Train the model using the training sets
knn.fit(X_train, y_train)
#Predict the response for test dataset
#print("Response for test dataset:")
y_pred = knn.predict(X_test)
print(knn.predict[1,.3,1.5,1.5])

#x_train= X_train.reshape(-1, 1)
#y_train= y_train.reshape(-1, 1)
#x_test = X_test.reshape(-1, 1)
#row = [1,.3,1.5,1.5]
#y_pred2 = knn.predict(row)
print(y_pred)

#test sample : row = [1,.3,1.5,1.5]