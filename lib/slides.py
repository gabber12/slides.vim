import mistune
import pyfiglet
from subprocess import call
import tempfile
import os

class SlidesConvertor(object):

    def __init__(self, renderer):
        self.renderer = renderer

    def output(self, text):
        return self.renderer.output(text)


class VimRenderer(mistune.Renderer):

    def __init__(self, padding=0):
        super(VimRenderer, self).__init__()
        self.padding = padding

    def placeholder(self):
        return ' '*self.padding

    def header(self, text, level, raw):
        if level == 1:
            text = pyfiglet.Figlet(font='block').renderText(text)
        if level == 2:
            text = pyfiglet.Figlet().renderText(text)
        return text

    def list(self, body, ordered):
        return body

    def list_item(self, body):
        return body

    def paragraph(self, body):
        return body


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


class FileReader(object):
    def __init__(self, filename):
        self.filename = filename

    def getText(self):
        with open(self.filename, 'r') as f:
            return f.read()


class Slides(object):

    def __init__(self, reader, renderer, presenter):
        self.renderer = renderer
        self.presenter = presenter
        self.reader = reader

    def _preprocess(self, text):
        return text.split("\n\n\n")

    def genrate(self):
        slidesText = self._preprocess(self.reader.getText())
        parsed_slides_text = []
        for each in slidesText:
            parsed_slides_text.append(self.renderer.output(each))
        return parsed_slides_text

    def start(self):
        self.presenter.present(self.genrate())


if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser(
        description='Do Presentation right from vim')
    parser.add_argument(
        'file',  type=str,
        help='The presentation markdown file')
    parser.add_argument(
        '--pretend', default=False, type=bool,
        help='If mentioned dumps the transformed output')
    args = parser.parse_args()
    convertor = mistune.Markdown(renderer=VimRenderer())
    c = Slides(FileReader(args.file), SlidesConvertor(convertor),
               VimPresenter())
    c.start()
