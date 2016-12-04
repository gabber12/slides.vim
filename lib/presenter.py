import os
import tempfile

class SlidePresenter(object):

    def __init__(self):
        pass

    def present(self, slides):
        i = 0
        for slide in slides:
            with open(os.path.join(tempfile.gettempdir(), str(i)+".md"), 'w') as f:
                f.write(slide)
                i += 1


class VimPresenter(SlidePresenter):
    def __init__(self):
        super(VimPresenter, self).__init__()

    def present(self, slides):
        super(VimPresenter, self).present(slides)
        call(['vim']+[os.path.join(tempfile.gettempdir(), str(num)+".md") for num in xrange(len(slides))])
