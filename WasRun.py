from TestCase import *


class WasRun(TestCase):

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1