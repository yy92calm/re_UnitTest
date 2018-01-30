import unittest

class reTestCase(unittest.TestCase):
    def setUp(self):
        print "start app"

    def tearDown(self):
        print "stop app"