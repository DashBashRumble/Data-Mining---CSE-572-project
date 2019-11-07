from LogisticRegression import LogReg
from DecisionTree import DecisionTree
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

from sklearn.metrics import classification_report, confusion_matrix


class Classification:
    def __init__(self, classifier_name, data, labels):
        self.x = data
        self.y = labels
        self.classifier_name = classifier_name
        self.clf = None
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.test_train_split()
        self.y_pred = None

    def test_train_split(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.4,
                                                                                shuffle=True, random_state=43)

    def get_classifier_object(self):
        if self.classifier_name == 'LogReg':
            self.clf = LogReg(self.x_train, self.y_train, self.x_test, self.y_test)
            self.clf.train()
            self.y_pred = self.clf.predict()
        elif self.classifier_name == 'DeciTree' :
            self.clf = DecisionTree(self.x_train, self.y_train, self.x_test, self.y_test)
            self.clf.train()
            self.y_pred = self.clf.predict()
        elif self.classifier_name == 'svm' :
            self.clf = DecisionTree(self.x_train, self.y_train, self.x_test, self.y_test)
            self.clf.train()
            self.y_pred = self.clf.predict()

    def get_metrics(self):
        print('classifier'+self.classifier_name)
        print('Accuracy score', accuracy_score(self.y_test, self.y_pred))
        print('Precision', precision_score(self.y_test, self.y_pred))
        print('Recall', recall_score(self.y_test, self.y_pred))
        print('F1 score', f1_score(self.y_test, self.y_pred))
        # print('confusion matrix')
        # print(confusion_matrix(self.y_test, self.y_pred))
        # print(classification_report(self.y_test, self.y_pred))



