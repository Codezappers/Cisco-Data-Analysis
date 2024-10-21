#This here is the decision tree classifier model from scikit-Learn library, the question is to find any three more models from the same package that could fit the data and generate the closest and most accurate prediction

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female','female','female','male','male','male','female','male', 'female','male']

# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, Y)
# prediction = clf.predict([[190, 70, 43]])

# rfc = RandomForestClassifier()
# rfc = rfc.fit(X, Y)
# prediction = rfc.predict([[190, 70, 43]])

lr = LogisticRegression()
lr = lr.fit(X, Y)
prediction = lr.predict([[190, 70, 43]])


print(prediction)