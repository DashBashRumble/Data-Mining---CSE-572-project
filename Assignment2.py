from preprocessing import Preprocess
from features import Features
from classification import Classification
import numpy as np

meal_data_filename = input("Please specify the file path of meal data file:\n")

no_meal_data_filename = input("Please specify the file path of no meal data file:\n")

cgm_meal_preprocess = Preprocess(meal_data_filename)
cgm_meal = cgm_meal_preprocess.get_dataframe()
cgm_meal_feature_obj = Features(cgm_meal)
cgm_meal_feature_obj.compute_features()
cgm_meal_final_features = cgm_meal_feature_obj.pca_decomposition().tolist()
y_meal = [1]*len(cgm_meal_final_features)

cgm_no_meal_preprocess = Preprocess(no_meal_data_filename)
cgm_no_meal = cgm_no_meal_preprocess.get_dataframe()
cgm_no_meal_feature_obj = Features(cgm_no_meal)
cgm_no_meal_feature_obj.compute_features()
cgm_no_meal_features = cgm_no_meal_feature_obj.get_features()
cgm_no_meal_final_features = cgm_meal_feature_obj.pca.transform(cgm_no_meal_features).tolist()
y_no_meal = [0]*len(cgm_no_meal_features)

for no_meal_feature in cgm_no_meal_final_features:
    cgm_meal_final_features.append(no_meal_feature)

y_meal += y_no_meal
print(len(cgm_meal_final_features), len(y_meal))
clf = Classification('LogReg', cgm_meal_final_features, y_meal)
clf.get_classifier_object()
clf.get_metrics()



