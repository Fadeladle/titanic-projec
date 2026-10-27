import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("train.csv")



#make FamilySize
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


#Extract Title from name
titles = []

for name in df["Name"]:
    title = name.split(",")[1].split(".")[0].strip()
    titles.append(title)

df["Title"] = titles



common_titles = ["Mr", "Miss", "Mrs", "Master"]

df["Title"] = df["Title"].where(
    df["Title"].isin(common_titles),
    "Other"
)


# =========================
#Cleaning Data
# =========================


df.drop(
    columns=[
        "PassengerId",
        "Name",
        "Ticket",
        "Cabin"
    ],
    inplace=True
)



df["Age"] = df.groupby(
    ["Sex", "Pclass"]
)["Age"].transform(
    lambda x: x.fillna(x.mean())
)



df["Embarked"] = df["Embarked"].fillna("S")


# =========================
# cut x,y
# =========================

X = df.drop("Survived", axis=1)
y = df["Survived"]


# =========================
#convert string to namieric
# =========================

X = pd.get_dummies(
    X,
    columns=["Sex", "Embarked", "Title"],
    dtype=int
)


# =========================
#spliting Data
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train:", X_train.shape)
print("Test:", X_test.shape)


# =========================
# 7. Logistic Regression
# =========================

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nLogistic Regression")
print("Accuracy:", accuracy_score(y_test, y_pred))

print(
    classification_report(
        y_test,
        y_pred
    )
)


# =========================
# 8. Decision Tree
# =========================

model2 = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model2.fit(X_train, y_train)

y_pred2 = model2.predict(X_test)

print("\nDecision Tree")
print("Accuracy:", accuracy_score(y_test, y_pred2))

print(
    classification_repot(
        y_test,
        y_pred2
    )
)
