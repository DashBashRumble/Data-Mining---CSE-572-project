from preprocessing import Preprocess
from features import Features


cgm_meal_pat_1_preprocess = Preprocess('./MealNoMealData/mealData1.csv')
cgm_meal_pat_1 = cgm_meal_pat_1_preprocess.get_dataframe()
print(cgm_meal_pat_1)
cgm_meal_pat_1_feature_obj = Features(cgm_meal_pat_1)
cgm_meal_pat1_features = cgm_meal_pat_1_feature_obj.compute_features()

cgm_meal_pat1_final_features = cgm_meal_pat_1_feature_obj.pca_decomposition()

