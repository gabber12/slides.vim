import unittest
from slides import Slides, VimRenderer, SlidesConvertor, SlidePresenter
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
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["dsadsa"], s.genrate())

    def test_h2_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsadsa\n---")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(['     _               _           \n  __| |___  __ _  __| |___  __ _ \n / _` / __|/ _` |/ _` / __|/ _` |\n| (_| \\__ \\ (_| | (_| \\__ \\ (_| |\n \\__,_|___/\\__,_|\\__,_|___/\\__,_|\n                                 \n'], s.genrate())

    def test_h1_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsadsa\n===")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["                                                            \n      _|                            _|                      \n  _|_|_|    _|_|_|    _|_|_|    _|_|_|    _|_|_|    _|_|_|  \n_|    _|  _|_|      _|    _|  _|    _|  _|_|      _|    _|  \n_|    _|      _|_|  _|    _|  _|    _|      _|_|  _|    _|  \n  _|_|_|  _|_|_|      _|_|_|    _|_|_|  _|_|_|      _|_|_|  \n                                                            \n                                                            \n"], s.genrate())


class TestListMethods(unittest.TestCase):

    def test_ol_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="1. dsadsa")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["dsadsa"], s.genrate())

    def test_ul_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="* dsadsa")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["dsadsa"], s.genrate())


class TestSlidesMethods(unittest.TestCase):

    def test_multiple_pages_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="1. dsa\n\n\nabc")
        markdown = Markdown(renderer=VimRenderer())
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["dsa", "abc"], s.genrate())


class TestPadding(unittest.TestCase):

    def test_multiple_pages_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa")
        markdown = Markdown(renderer=VimRenderer(5))
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual([" "*10+"dsa"], s.genrate())

    def test_multiple_pages2_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa")
        markdown = Markdown(renderer=VimRenderer(2))
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual([" "*4+"dsa" ], s.genrate())


class TestBasePresentor(unittest.TestCase):
    def test_files_exists(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa\n\n\nds")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer(8))), SlidePresenter())
        s.start()
        import os
        self.assertTrue(os.path.isfile('/tmp/rand0'))
        self.assertTrue(os.path.isfile('/tmp/rand1'))


if __name__ == '__main__':
    unittest.main()
