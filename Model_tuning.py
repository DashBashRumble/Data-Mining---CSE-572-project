from train_preprocess import get_data
from classification import Classification
import numpy as np
import pickle


x, y = get_data()
print(len(x), len(y))
# clf_logreg = Classification('LogReg', x, y)
# clf_logreg.get_classifier_object()
# clf_logreg.get_metrics()
# pickle.dump(clf_logreg.get_classifier(), open('LogReg_model.pkl', 'wb'))
# print()

# clf_deci = Classification('DeciTree', x, y)
# clf_deci.get_classifier_object()
# clf_deci.get_metrics()
# pickle.dump(clf_deci.get_classifier(), open('DeciTree_model.pkl', 'wb'))
# print()

# clf_svm = Classification('svm', x, y)
# clf_svm.get_classifier_object()
# clf_svm.get_metrics()
# pickle.dump(clf_svm.get_classifier(), open('svm_model.pkl', 'wb'))
# print()
clf_rforest = Classification('RForest', x, y)
clf_rforest.get_classifier_object()
clf_rforest.get_metrics()
pickle.dump(clf_rforest.get_classifier(), open('RForest_model.pkl', 'wb'))
print()

clf = Classification('XGB', np.array(x), np.array(y))
clf.get_classifier_object()
clf.get_metrics()
pickle.dump(clf.get_classifier(), open('XGBoost_model.pkl', 'wb'))
print()

clf = Classification('NaiveBayes', np.array(x), np.array(y))
clf.get_classifier_object()
clf.get_metrics()
pickle.dump(clf.get_classifier(), open('NaiveBayes_model.pkl', 'wb'))
print()

clf = Classification('AdaBoost', np.array(x), np.array(y))
clf.get_classifier_object()
clf.get_metrics()
pickle.dump(clf.get_classifier(), open('Adaboost_model.pkl', 'wb'))
print()

