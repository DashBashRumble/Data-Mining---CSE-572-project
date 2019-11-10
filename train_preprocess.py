import os
from preprocessing import Preprocess
from features import Features


def get_data():
    files = os.listdir('./MealNoMealData')
    meal_data_files = []
    no_meal_data_files = []
    for file in files:
        if 'Nomeal' in file:
            no_meal_data_files.append(os.path.join('./MealNoMealData', file))
        else:
            meal_data_files.append(os.path.join('./MealNoMealData', file))

    data = []

    labels = []
    for meal_data_file, no_meal_data_file in zip(meal_data_files, no_meal_data_files):

        preprocess_obj = Preprocess(meal_data_file)
        meal_df = preprocess_obj.get_dataframe()
        meal_features = Features(meal_df)
        meal_features.compute_features()
        # temp_meal_features = meal_features.pca_decomposition().tolist()
        temp_meal_features = meal_features.get_features()
        labels += [1]*len(temp_meal_features)

        preprocess_obj_ = Preprocess(no_meal_data_file)
        no_meal_df = preprocess_obj_.get_dataframe()
        no_meal_features = Features(no_meal_df)
        no_meal_features.compute_features()
        no_meal_features_ = no_meal_features.get_features()
        # no_meal_final_features = meal_features.pca.transform(no_meal_features_).tolist()
        no_meal_final_features = no_meal_features_
        labels += [0]*len(no_meal_features_)

        for no_meal_feature in no_meal_final_features:
            temp_meal_features.append(no_meal_feature)

        for meal_no_meal_feature in temp_meal_features:
            data.append(meal_no_meal_feature)

    return data, labels

