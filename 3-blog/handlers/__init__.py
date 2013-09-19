
import os
import webapp2

import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + r'/../templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseRequestHandler(webapp2.RequestHandler):

    def write(self, what):
        self.response.write(what)

    def render(self, template_name, **kwargs):
        rendered_template = get_rendered_template(template_name, **kwargs)
        self.write(rendered_template)

    def get_argument(self, argument_name):
        return self.request.get(argument_name)


def get_rendered_template(template_name, **kwargs):

    template = JINJA_ENVIRONMENT.get_template(template_name)
    return template.render(**kwargs)