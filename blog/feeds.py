from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

"""
This code defines a custom RSS feed for a blog using 
django.contrib.syndication.views.Feed



"""


class LatestPostsFeed(Feed):
    # This is the title that will appear in the RSS feed,
    # typically as the name of the blog.
    title = "My Blog"

    # This is the URL where the full content of the blog posts can be found.
    link = reverse_lazy("blog:post_list")

    # This is a short description that will appear in the RSS
    # feed to tell users what kind of content the feed is offering
    description = "New posts of my blog."

    # This method defines the items (blog posts) that will be included in the RSS feed.
    def items(self):
        # Post.published.all() presumably fetches all the published blog posts,
        # and [:5] limits the result to the first 5 posts (i.e., the 5 most recent posts).
        return Post.published.all()[:5]

    # This method defines the title of each individual RSS feed item.
    def item_title(self, item):
        return item.title

    # This method defines the description (or content) of each RSS feed item.
    def item_description(self, item):
        return truncatewords(item.body, 30)
