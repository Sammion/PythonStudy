# @author：Sam
# @date:2018-01-05
# desc：练习随机森林算法使用
# pip install -U scikit-learn
from sklearn.ensemble import RandomForestClassifier

x = [[0, 0], [1, 1]]
y = [0, 1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(x, y)





