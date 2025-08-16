from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):#Model representing a single blog post.
    title=models.CharField(max_length=200)
    content=models.TextField()
    # The ForeignKey connects a Post to a User.
    # on_delete=models.CASCADE means if a User is deleted, all their posts are also deleted.
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Comment(models.Model):#Model representing a comment on a blog post.
       # The ForeignKey connects a Comment to a Post.
       post=models.ForeignKey(Post,on_delete=models.CASCADE)
       # The ForeignKey connects a Comment to a User (the person who commented).
       author=models.ForeignKey(User,on_delete=models.CASCADE)
       content=models.TextField(max_length=100000)
       created_at=models.DateTimeField(auto_now_add=True)
       def __str__(self):
            return f'Comment by {self.author} on {self.post}'

# related_name='comments' allows us to get all comments for a post easily.
                  