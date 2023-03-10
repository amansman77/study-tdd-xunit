from TestCase import TestCase


class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = 'setUp '

    def tearDown(self):
        self.log = self.log + 'tearDown '

    def testMethod(self):
        self.wasRun = 1 
        self.log = self.log + 'testMethod '

    def testBrokenMethod(self):
        raise Exception
