import unittest
from slides import Slides, VimRenderer, SlidesConvertor, VimRCGenerator
from presenter import SlidePresenter, VimPresenter
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

class TestVimPresentor(unittest.TestCase):
    def test_arguments_has_rc_file(self):
        thing = MockReader()
        thing.generateFile = MagicMock(return_value="/tmp/rand.rc")
        s = VimPresenter(thing).withRC()
        self.assertIn('-u', s.vim_args)
        self.assertIn("/tmp/rand.rc", s.vim_args)

    def test_arguments_has_rc_file(self):
        thing = VimPresenter(VimRCGenerator())
        thing.withRC = MagicMock()
        thing._get_command(2)
        thing.withRC.assert_called_once()

if __name__ == '__main__':
    unittest.main()
