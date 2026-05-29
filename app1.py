import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score



# load the dataset
data = pd.read_csv('car_update.csv')



# Show first 5 rows of a dataset
data.head()

# Checking misiing values
data.isnull().sum()

# Stasticial Methods
data.describe()

# Shape of a dataset
data.shape



# rename the data to a numerical values
data['buying'] = data['buying'].map({'vhigh':0, 'high':1,'med':2,'low':3})
data['maint'] = data['maint'].map({'vhigh':0, 'high':1,'med':2,'low':3})
data['lug_boot'] = data['lug_boot'].map({'small':0, 'med':1,'big':2})
data['safety'] = data['safety'].map({'low':0,'med':1,'high':2})
data['class'] = data['class'].map({'unacc':0,'acc':1,'good':2,'vgood':3})
data['doors'] = data['doors'].map({'5more':0})
data['persons'] = data['persons'].map({'more':0})



# Data Visulaization
data['buying'].hist()
data['maint'].hist()
data['class'].hist()
data.plot(kind='scatter', x='buying', y='safety', alpha=0.2, grid=True)
plt.show()


# Droping the safety Columns
X = data.drop('safety', axis=1)
Y = data['safety'] 


# Printing X and Y
print(X)
print(Y)




# Splitting the dataset into Training data and Testing data
X_train, Y_train, X_test, Y_test = train_test_split(X, Y, test_size=0.3,random_state=42)


print(X.shape)

print(X_test.shape)

print(X_train.shape)


# Train a model
# RandomForestClassifier

Rd = RandomForestClassifier()
Rd.fit(X_train, Y_train)

# Training the model of Trining Data
train_data = Rd.predict(X_train)

accuracy_score = accuracy_score(Y_train, train_data)

print('Accuray_training', accuracy_score)


# Training the Model of Testing Data
test_data = Rd.predict(X_test)
accuracy_score = accuracy_score(Y_test, test_data)

print('Accuracy_testing', accuracy_score)


# DecisionTreeClassifier
Dt = DecisionTreeClassifier()
Dt.fit(X_train. Y_train)

# Train the model of Training data
train_data1 =Dt.predict(X_train) 

training_accuracy = accuracy_score(Y_train, train_data1)
print('training_accuracy', training_accuracy)


# Train the Model of Testing data
test_data1 = Dt.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_data1)
print('test_accuarcy', test_accuracy)












