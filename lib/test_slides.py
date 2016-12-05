import unittest
from slides import Slides, VimRenderer, SlidesConvertor
from presenter import SlidePresenter
from mock import MagicMock
from mistune import Markdown
from test_mocks import *



class TestHeaderMethods(unittest.TestCase):


    def test_h3_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="### dsadsa\n")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(['dsadsa\n------\n'], s.genrate())

    def test_h2_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="## dsadsa\n")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer())), None)
        self.assertEqual(['dsadsa\n======\n'], s.genrate())


class TestListMethods(unittest.TestCase):
    def test_ul_ol_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="1. dsadsa\n    * fgh\n    2. dsa")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["\n- dsadsa\n\t- fgh\n- dsa\n"], s.genrate())

    def test_ol_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="1. dsadsa\n2. dsa")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["\n- dsadsa\n- dsa\n"], s.genrate())

    def test_ul_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="* dsadsa\n* abc")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["\n- dsadsa\n- abc\n"], s.genrate())

    def test_nestedul_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="* dsadsa\n    * dsa")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["\n- dsadsa\n\t- dsa\n"], s.genrate())

    def test_nested3ul_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="* dsadsa\n    * dsa\n        * jkl")
        markdown = Markdown(renderer=VimRenderer())
        s = Slides(thing, SlidesConvertor(markdown), None)
        self.assertEqual(["\n- dsadsa\n\t- dsa\n\t\t- jkl\n"], s.genrate())

class TestSlidesMethods(unittest.TestCase):

    def test_multiple_pages_generation(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa\n\n\nabc")
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
