import unittest
from slides import Slides, VimRenderer, SlidesConvertor
from presenter import SlidePresenter
from mock import MagicMock
from mistune import Markdown
from test_mocks import *


class TestBasePresentor(unittest.TestCase):
    def test_files_exists(self):
        thing = MockReader()
        thing.getText = MagicMock(return_value="dsa\n\n\nds")
        s = Slides(thing, SlidesConvertor(Markdown(renderer=VimRenderer(8))), SlidePresenter())
        s.start()
        import os, tempfile
        self.assertTrue(os.path.isfile(os.path.join(tempfile.gettempdir(), '0.md')))
        self.assertTrue(os.path.isfile(os.path.join(tempfile.gettempdir(), '1.md')))


if __name__ == '__main__':
    unittest.main()
