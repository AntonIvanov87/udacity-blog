import os
import re
import urllib

import jinja2
import webapp2

USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')

PASSWORD_RE = re.compile(r'^.{3,20}$')

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class SignupPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(get_signup_html())

    def post(self):

        username = self.request.get('username')
        username_error = get_username_error(username)

        password = self.request.get('password')
        password_error = get_password_error(password)

        verify = self.request.get('verify')
        verify_error = get_verify_error(password, verify)

        email = self.request.get('email')
        email_error = get_email_error(email)

        if username_error or password_error or verify_error or email_error:
            html = get_signup_html(
                username=username,
                username_error=username_error,
                password_error=password_error,
                verify_error=verify_error,
                email=email,
                email_error=email_error
            )
            self.response.write(html)
        else:
            query = urllib.urlencode({'username': username})
            self.redirect('/welcome?' + query)


def get_username_error(username):
    if not username:
        return 'fill in username'
    elif not USER_RE.match(username):
        return 'username is not valid'
    else:
        return ''


def get_password_error(password):
    if not password:
        return 'fill in password'
    elif not PASSWORD_RE.match(password):
        return 'password is not valid'
    else:
        return ''


def get_verify_error(password, verify):
    if not verify:
        return 'fill in password again'
    elif password and verify != password:
        return 'password does not match'
    else:
        return ''


def get_email_error(email):
    if email and not EMAIL_RE.match(email):
        return 'email is not valid'
    else:
        return ''


def get_signup_html(username='', username_error='', password_error='', verify_error='', email='', email_error=''):
    template = JINJA_ENVIRONMENT.get_template('signup.html')
    return template.render(
        username=username,
        username_error=username_error,
        password_error=password_error,
        verify_error=verify_error,
        email=email,
        email_error=email_error
    )


class WelcomePage(webapp2.RequestHandler):

    def get(self):
        username = self.request.get('username')
        self.response.write(get_welcome_html(username))


def get_welcome_html(username):

    template = JINJA_ENVIRONMENT.get_template('welcome.html')
    return template.render(
        username=username
    )


application = webapp2.WSGIApplication(
    [
        ('/welcome', WelcomePage),
        ('/.*', SignupPage)
    ],
    debug=True
)