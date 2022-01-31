# importing scikit learn library

import sklearn

from sklearn import tree

# features of an apple and an orange
# 1 - smooth texture , 2 - bumpy texture
features = [[1,150],[2,50],[2,60],[1,120],[1,122],[2,80]]

# matching texture to products
label = ['apple','orange','orange','apple','apple','orange']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features,label)

print(clf.predict([[2,40]]))
