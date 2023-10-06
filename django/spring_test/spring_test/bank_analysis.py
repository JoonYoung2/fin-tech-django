import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

def init():
    print("초기화 용도")
    df = pd.read_csv("C:/Users/user/Desktop/jyseo/0.공유자료/0.핀테크/django/django/bank_cleaning.csv")
    print(df.head())
    
    features = ['age', 'duration', 'campaign', 'pdays', 'previous']
    label = 'y'
    X, y = df[features], df[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    gbc = GradientBoostingClassifier()
    gbc.fit(X_train, y_train)
    print("train : ", gbc.score(X_train, y_train))
    print("test : ", gbc.score(X_test, y_test))

    return gbc