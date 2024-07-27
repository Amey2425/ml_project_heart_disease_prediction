import numpy as np 
import pandas as pd 
import sklearn 
import pickle
dataset = pd.read_csv('project/heart.csv')
X = dataset.iloc[ : , :-1]
y = dataset.iloc[ : , -1]
print(dataset.count())
dataset.drop_duplicates(inplace=True)
print(dataset.count())
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=42)


from sklearn.model_selection import GridSearchCV 
from sklearn.metrics import accuracy_score ,confusion_matrix
param_grid = {
    'n_estimators':[50,100,200],
    'max_depth': [None,10,20],
    'min_samples_split': [2,5],
    'min_samples_leaf':[1,2]
}
grid_search = GridSearchCV(estimator=classifier,param_grid=param_grid,cv = 5)
grid_search.fit(X_train,y_train)

best_params = grid_search.best_params_ 
print(f"Best parameters found : {best_params}")

classifier_tuned = RandomForestClassifier(**best_params,random_state=42)
classifier_tuned.fit(X_train,y_train)

#save the model and scaler to disk
with open('model.pkl','wb') as model_file:
    pickle.dump(classifier_tuned,model_file)
    
with open('scaler.pkl','wb') as scaler_file:
    pickle.dump(scaler,scaler_file)
    


y_pred_tuned = classifier_tuned.predict(X_test)
accuracy_tuned = accuracy_score(y_test,y_pred_tuned)
cm = confusion_matrix(y_pred_tuned,y_test)
print(cm)

print(f"Accuracy after tuning :{accuracy_tuned}")