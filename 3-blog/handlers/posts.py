
import handlers
from entities.post import Post


class PostsHandler(handlers.BaseRequestHandler):

    def get(self):

        posts = Post.gql("ORDER BY date DESC LIMIT 10")
        self.render(posts=posts)

    def render(self, **kwargs):
        handlers.BaseRequestHandler.render(self, 'posts.html', **kwargs)
