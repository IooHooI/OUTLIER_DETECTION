import unittest
from source.code.MyDBCAN import MyDBCAN
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline


class TestMyDBSCAN(unittest.TestCase):

    def setUp(self):
        # TODO: generate train/test data frames
        self.my_dbscan = MyDBCAN()

    def test_my_dbscan(self):
        dbscan_pipeline = Pipeline([
            ('reduce', PCA(n_components=2, random_state=42)),
            ('fit', self.my_dbscan)
        ])
        # TODO: generate train/test data frames


if __name__ == '__main__':
    unittest.main()
