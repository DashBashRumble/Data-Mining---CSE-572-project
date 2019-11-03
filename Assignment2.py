from preprocessing import Preprocess
from features import Features

meal_data_filename = input("Please specify the file path of meal data file:\n")

no_meal_data_filename = input("Please specify the file path of no meal data file:\n")

cgm_meal_preprocess = Preprocess(meal_data_filename)
cgm_meal = cgm_meal_preprocess.get_dataframe()
cgm_meal_feature_obj = Features(cgm_meal)
cgm_meal_feature_obj.compute_features()
cgm_meal_features = cgm_meal_feature_obj.get_features()
cgm_meal_final_features = cgm_meal_feature_obj.pca_decomposition()

cgm_no_meal_preprocess = Preprocess(no_meal_data_filename)
cgm_no_meal = cgm_no_meal_preprocess.get_dataframe()
cgm_no_meal_feature_obj = Features(cgm_no_meal)
cgm_no_meal_feature_obj.compute_features()
cgm_no_meal_features = cgm_no_meal_feature_obj.get_features()
print('cgm_nomeal_features', cgm_no_meal_features)
cgm_no_meal_final_features = cgm_meal_feature_obj.pca.transform(cgm_no_meal_features)
print(cgm_no_meal_final_features)