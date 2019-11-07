from train_preprocess import get_data
from classification import Classification
import numpy as np


x, y = get_data()
print(len(x), len(y))
clf = Classification('LogReg', x, y)
clf.get_classifier_object()
clf.get_metrics()

clf = Classification('DeciTree', x, y)
clf.get_classifier_object()
clf.get_metrics()

clf = Classification('svm', x, y)
clf.get_classifier_object()
clf.get_metrics()