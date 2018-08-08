from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.cluster import DBSCAN


class MyDBCAN(BaseEstimator, ClassifierMixin):

    def __init__(self):
        self.dbscan = DBSCAN()

    def fit(self, X, y=None):
        self.dbscan.fit(X)
        return self

    def predict(self, X, y=None):
        return self.dbscan.labels_
