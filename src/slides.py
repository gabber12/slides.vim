import mistune
import pyfiglet
from presenter import VimPresenter, VimRCGenerator


class SlidesConvertor(object):

    def __init__(self, renderer):
        self.renderer = renderer

    def output(self, text):
        out = self.renderer.output(text)
        import re
        out = re.sub(r"\n\t(\S)", r"\n\1", out)
        out = out.replace("\t\t", "\t")
        return out


class VimRenderer(mistune.Renderer):

    def __init__(self, padding=0):
        super(VimRenderer, self).__init__()
        self.padding = padding

    def placeholder(self):
        return ' '*self.padding

    def header(self, text, level, raw):
        if level == 1:
            text = pyfiglet.Figlet().renderText(text)
        elif level == 2:
            text = text+"\n"+"="*len(text)+"\n"
        else:
            text = text+"\n"+"-"*len(text)+"\n"
        return text

    def list(self, body, ordered):
        body = body.replace('\t', '\t\t')
        return "\n\t"+body

    def list_item(self, body):
        return "- "+body.rstrip("\n")+"\n"

    def paragraph(self, body):
        return body


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
            out = self.renderer.output(each)
            parsed_slides_text.append(out)
        return parsed_slides_text

    def start(self):
        self.presenter.present(self.genrate())


if __name__ == '__main__':
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
               VimPresenter(VimRCGenerator()))
    c.start()
