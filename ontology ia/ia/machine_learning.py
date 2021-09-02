from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn import tree
from os.path import isfile
import joblib

class learn:
    def __init__(self):
        self.filename = 'finalized_model.sav'
        if isfile(self.filename):
            loaded_model = joblib.load(self.filename)
            self.cls = loaded_model
        else:
            self.cls = tree.DecisionTreeClassifier()

    def test_split(self, array_test_x, array_test_y):
        X_train, X_test, y_train, y_test = train_test_split(
            array_test_x, array_test_y, random_state=1)
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def train_preprocessor(self, array_test_x, array_test_y):
        le = preprocessing.LabelEncoder()
        enc = OneHotEncoder(handle_unknown='ignore')
        processed_x = enc.fit_transform(array_test_x)
        processed_y = le.fit_transform(array_test_y)
        return (processed_x, processed_y)

    def preprocessor(self, array_x):
        enc = OneHotEncoder(handle_unknown='ignore')
        processed_x = enc.fit_transform(array_x)
        return processed_x

    def train_ia(self):
        self.cls.fit(self.X_train, self.y_train)

    def predict_test(self):
        score = self.cls.predict(self.X_test)
        self.rating(score)

    def predict(self, element):
        score = self.cls.predict(element)
        self.rating(score)

    def rating(self, score):
        file = open(f'./results/ontology_score.txt', "w+")
        file.write("The score array is - \n")
        file.writelines(str(score))

    def save_model(self):
        joblib.dump(self.cls, self.filename)