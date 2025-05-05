from sklearn.ensemble import RandomForestClassifier

def recommend_crop(X_train, y_train):
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf
