from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import pandas as pd
import joblib

df = pd.read_csv("CreditCardUpgrade.csv")
X = df.loc[:, ["Purchases","SuppCard"]]
Y = df.loc[:,"Upgraded"]

# Decision Tree
print("Decision Tree Classifier - Model")
model = tree.DecisionTreeClassifier(max_depth=2)
model.fit(X,Y)
pred = model.predict(X)
print(pred)
cm = confusion_matrix(Y,pred)
print(cm)
print("Decision Tree Classifier accuracy: {0} %".format(round(model.score(X,Y) * 100, 2)))
joblib.dump(model, "CART")

print("Decision Tree Classifier - Predict")
model = joblib.load("CART")
pred = model.predict([[20,1]])
print(pred)


# Random Forest
model = RandomForestClassifier(ccp_alpha=0.0384)
model.fit(X,Y)
pred = model.predict(X)
print(pred)
cm = confusion_matrix(Y,pred)
print(cm)
print("Random Forest Classifier accuracy: {0} %".format(round(model.score(X,Y) * 100, 2)))

joblib.dump(model, "RF")


# GradientBoostingClassifier
model = GradientBoostingClassifier(min_samples_split=30,random_state=260322)
model.fit(X,Y)
pred = model.predict(X)
print(pred)
cm = confusion_matrix(Y,pred)
print(cm)
print("Gradient Boosting Classifier accuracy: {0} %".format(round(model.score(X,Y) * 100, 2)))

joblib.dump(model, "GBC")