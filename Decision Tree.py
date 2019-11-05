from preprocessing import Preprocess
from features import Features
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

path='Data/'
X = np.array([[0,0,0,0,0]])
y = [0]

for i in range(5):
    meal_data_filename = 'mealData'+str(i+1)+'.csv'
    cgm_meal_preprocess = Preprocess(path + meal_data_filename)
    cgm_meal = cgm_meal_preprocess.get_dataframe()
    cgm_meal_feature_obj = Features(cgm_meal)
    cgm_meal_feature_obj.compute_features()
    cgm_meal_features = cgm_meal_feature_obj.get_features()
    cgm_meal_final_features = cgm_meal_feature_obj.pca_decomposition()

    no_meal_data_filename = 'Nomeal'+str(i+1)+'.csv'
    cgm_no_meal_preprocess = Preprocess(path + no_meal_data_filename)
    cgm_no_meal = cgm_no_meal_preprocess.get_dataframe()
    cgm_no_meal_feature_obj = Features(cgm_no_meal)
    cgm_no_meal_feature_obj.compute_features()
    cgm_no_meal_features = cgm_no_meal_feature_obj.get_features()
    cgm_no_meal_final_features = cgm_meal_feature_obj.pca.transform(cgm_no_meal_features)

    label_meal = [1]*len(cgm_meal_final_features)
    label_nomeal = [0]*len(cgm_no_meal_final_features)

    X_file = np.concatenate((cgm_meal_final_features, cgm_no_meal_final_features), axis=0)
    y_file = label_meal + label_nomeal

    X = np.concatenate((X, X_file), axis=0)
    y = y + y_file

#removing the dummy values we added
X = X[1:]
y = y[1:]

#Splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
# Training Decision Tree Classifer
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))