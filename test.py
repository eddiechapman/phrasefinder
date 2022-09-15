import unittest

from phrasefinder import PhraseFinder


class TestPhraseFinder(unittest.TestCase):
    def setUp(self):
        self.text = "Back pain in adolescents is an under-studied condition"

    def test_search_single(self):
        finder = PhraseFinder("back pain", text=self.text)
        self.assertEqual(finder.search(), [(0, 9)])

    def test_search_multi(self):
        finder = PhraseFinder("back pain", "adolescents", text=self.text)
        self.assertEqual(finder.search(), [(0, 9), (13, 24)])

    def test_search_single_missing(self):
        finder = PhraseFinder("missing phrase", text=self.text)
        self.assertEqual(finder.search(), [])

    def test_search_multi_missing_one(self):
        finder = PhraseFinder("back pain", "missing phrase", text=self.text)
        self.assertEqual(finder.search(), [])


if __name__ == "__main__":
    unittest.main()
