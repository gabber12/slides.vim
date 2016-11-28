import unittest
from slides import Slides, VimRenderer, SlidesConvertor
from mock import MagicMock
from mistune import Markdown


class MockReader(object):

    pass


class MockWriter(object):

    pass



class TestHeaderMethods(unittest.TestCase):

    def test_h3_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="### dsadsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(["dsadsa"], s.genrate())

    def test_h2_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsadsa\n---")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(['     _               _           \n  __| |___  __ _  __| |___  __ _ \n / _` / __|/ _` |/ _` / __|/ _` |\n| (_| \\__ \\ (_| | (_| \\__ \\ (_| |\n \\__,_|___/\\__,_|\\__,_|___/\\__,_|\n                                 \n'], s.genrate())

    def test_h1_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsadsa\n===")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(["                                                            \n      _|                            _|                      \n  _|_|_|    _|_|_|    _|_|_|    _|_|_|    _|_|_|    _|_|_|  \n_|    _|  _|_|      _|    _|  _|    _|  _|_|      _|    _|  \n_|    _|      _|_|  _|    _|  _|    _|      _|_|  _|    _|  \n  _|_|_|  _|_|_|      _|_|_|    _|_|_|  _|_|_|      _|_|_|  \n                                                            \n                                                            \n"], s.genrate())


class TestListMethods(unittest.TestCase):

    def test_ol_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="1. dsadsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(["dsadsa"], s.genrate())

    def test_ul_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="* dsadsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(["dsadsa"], s.genrate())

class TestSlidesMethods(unittest.TestCase):

    def test_multiple_pages_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="1. dsa\n\n\nabc")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(["dsa", "abc"], s.genrate())

class TestPadding(unittest.TestCase):

    def test_multiple_pages_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer(5))), None)
        self.assertEqual([" "*10+"dsa" ], s.genrate())
    def test_multiple_pages2_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer(2))), None)
        self.assertEqual([" "*4+"dsa" ], s.genrate())
    def test_multiple_pages23_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer(4))), None)
        self.assertEqual([" "*8+"dsa" ], s.genrate())
    def test_multiple_pagesa42_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer(7))), None)
        self.assertEqual([" "*14+"dsa" ], s.genrate())


if __name__ == '__main__':
    unittest.main()
