#importing library finctions
import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split #split dataset into test and train cases
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score,classification_report
from sklearn.ensemble import RandomForestClassifier

def get_data(filename):
    dataset=pd.read_csv(filename)
    X=dataset.iloc[:,0:8]#select all attribute columns
    y=dataset.iloc[:,8]#select outputs11
    return X,y
X,y=get_data('diabetes.csv')
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0, test_size=0.30)

clf =RandomForestClassifier(n_estimators=100,random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Random Forest Model Accuracy")
print(accuracy_score(y_test,y_pred))

print(classification_report(y_test,y_pred))
cm=confusion_matrix(y_test,y_pred)#comparing with test cases
print ("confusion matrix")
print (cm)
print ("Accuracy:")
print (accuracy_score(y_test,y_pred))

test_output=[[ 5, 116,74 ,1,1,25.6,1.201,30]]#test output
test_output=np.array(test_output).reshape(1,-1)
test_output=test_output.astype(np.float64)
pred=clf.predict(test_output)
print (pred)
if (pred==1):
    print ("has diabeties")
else :
    print ("no diabeties")
