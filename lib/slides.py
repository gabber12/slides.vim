import mistune
import pyfiglet

class SlidesConvertor(object):

    def __init__(self, renderer):
        self.renderer = renderer

    def output(self, text):
        return self.renderer.output(text)


class VimRenderer(mistune.Renderer):
    def __init__(self, padding = 0):
        super(VimRenderer, self).__init__()
        self.padding = padding

    def placeholder(self):
        return ' '*self.padding

    def header(self, text, level, raw):
        if level == 1:
            text  = pyfiglet.Figlet(font='block').renderText(text)
        if level == 2:
            text  = pyfiglet.Figlet().renderText(text)
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
            with open('/tmp/rand'+str(i), 'w') as f:
                f.write(slide)
                i+=1



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

    c = Slides()
    c.generate()
