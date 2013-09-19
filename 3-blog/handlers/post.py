
import handlers
from entities.post import Post


class PostHandler(handlers.BaseRequestHandler):

    def get(self, post_id_str):
        post_id = int(post_id_str)
        post = Post.get_by_id(post_id)
        self.render(post=post)

    def render(self, **kwargs):
        handlers.BaseRequestHandler.render(self, 'post.html', **kwargs)