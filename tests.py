import unittest
from app import is_alive_host


class Test_is_alive_host(unittest.TestCase):

    def test_200(self):
        self.assertTrue(is_alive_host('https://httpstat.us/200'))

    def test_300(self):
        self.assertTrue(is_alive_host('https://httpstat.us/300'))

    def test_400(self):
        self.assertFalse(is_alive_host('https://httpstat.us/400'))
    
    def test_500(self):
        self.assertFalse(is_alive_host('https://httpstat.us/500'))


if __name__ == '__main__':
    unittest.main()