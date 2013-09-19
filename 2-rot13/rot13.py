import os

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(get_html(''))

    def post(self):
        text = self.request.get('text')
        new_text = rot13(text)

        self.response.write(get_html(new_text))


def get_html(text):
    template = JINJA_ENVIRONMENT.get_template('index.html')
    return template.render(text=text)


def rot13(text):
    return ''.join(
        map(lambda ch: _rot13_dict.get(ch, ch), text)
    )


def _get_rot13_range(start, end):
    return [(chr(i), chr(start + (i - start + 13) % 26))
            for i in range(start, end + 1)]


_rot13_dict = dict(_get_rot13_range(ord('a'), ord('z')) + _get_rot13_range(ord('A'), ord('Z')))


application = webapp2.WSGIApplication(
    [
        ('/.*', MainPage)
    ],
    debug=True
)