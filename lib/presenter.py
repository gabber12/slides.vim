import os
import tempfile
from subprocess import call


class SlidePresenter(object):

    def __init__(self):
        pass

    def present(self, slides):
        for sno, slide in enumerate(slides):
            with open(os.path.join(tempfile.gettempdir(), str(sno)+".md"), 'w') as f:
                f.write(slide)


class VimPresenter(SlidePresenter):

    def __init__(self, vim_rc_generator, vim_args=[]):
        super(VimPresenter, self).__init__()
        self.vim_args = vim_args
        self.vim_rc_generator = vim_rc_generator

    def withRC(self):
        temp_rc = self.vim_rc_generator.generateFile()
        self.vim_args += ['-u', temp_rc]
        return self

    def _get_command(self, num_slides):
        self.withRC()
        return ['vim'] + self.vim_args + [os.path.join(tempfile.gettempdir(), str(num)+".md") for num in xrange(num_slides)]

    def present(self, slides):
        super(VimPresenter, self).present(slides)
        call(self._get_command(len(slides)))

class VimRCGenerator(object):
    def __init__(self):
        self.rc_string = "set nonu"

    def generateFile(self):
        temp_vimrc = os.path.join(tempfile.gettempdir(), 'rand.vimrc')
        with open(temp_vimrc, 'w') as f:
            f.write(self.rc_string)
        return temp_vimrc
