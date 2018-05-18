import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pandas.read_csv(url, names=names)

# shape
print("*** printing shape ***")
print(dataset.shape)
print("*** printed shape ***")

# head
print("*** printing head 20 ***")
print(dataset.head(20))
print("*** printed head 20 ***")

# statistical descriptions
print("*** printing statistical descriptions ***")
print(dataset.describe())
print("*** printed statistical descriptions ***")

# class distribution
print("*** printing class distribution ***")
print(dataset.groupby("class").size())
print("*** printed class distribution ***")

# box and whisker plots
