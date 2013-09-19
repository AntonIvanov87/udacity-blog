#!/usr/bin/env python

import webapp2

import handlers.posts
import handlers.post
import handlers.newpost


app = webapp2.WSGIApplication([
    ('/newpost', handlers.newpost.NewPostHandler),
    ('/(\d+)', handlers.post.PostHandler),
    ('/', handlers.posts.PostsHandler)
], debug=True)
