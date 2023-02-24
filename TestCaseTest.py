from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun('testMethod')

    def testSetUp(self):
        self.test.run()
        assert 'setUp testMethod ' == self.test.log

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert 'setUp testMethod ' == test.log

TestCaseTest('testSetUp').run()
TestCaseTest('testTemplateMethod').run()