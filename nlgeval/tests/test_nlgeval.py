import unittest

from nlgeval import NLGEval


class TestNlgEval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n = NLGEval()

    def test_eval(self):
        actual = self.n.compute_individual_metrics(ref=['this is a test',
                                                        'this is also a test'],
                                                   hyp='this is a good test')
        print(actual)
        # TODO
        # self.assertEqual(1, actual)
