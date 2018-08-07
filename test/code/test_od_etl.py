import unittest
from source.code.od_etl import ODETL


class TestODETL(unittest.TestCase):

    def setUp(self):
        self.odetl = odetl = ODETL('../../data/datasets/')

    def test_get_raw_data(self):
        self.odetl.get_raw_data('http://www.dbs.ifi.lmu.de/research/outlier-evaluation/input/ALOI.tar.gz')


if __name__ == '__main__':
    unittest.main()
