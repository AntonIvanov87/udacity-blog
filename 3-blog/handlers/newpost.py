
import handlers
from entities.post import Post


class NewPostHandler(handlers.BaseRequestHandler):

    def get(self):
        self.render()

    def post(self):
        subject = self.get_argument('subject').strip()
        subject_error = get_subject_error(subject)

        content = self.get_argument('content').strip()
        content_error = get_content_error(content)

        if subject_error or content_error:
            self.render(
                subject=subject,
                subject_error=subject_error,
                content=content,
                content_error=content_error
            )

        else:
            blog_post = Post()
            blog_post.subject = subject
            blog_post.content = content
            blog_post.put()
            self.redirect('/{post_id}'.format(post_id=blog_post.key().id()))

    def render(self, **kwargs):
        handlers.BaseRequestHandler.render(self, 'newpost.html', **kwargs)


def get_subject_error(subject):
    if not subject:
        return 'subject is empty'
    else:
        return ''


def get_content_error(content):
    if not content:
        return 'content is empty'
    else:
        return ''