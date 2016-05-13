from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    commenter_name = models.CharField(max_length=50, null=True)
    commenter_ip = models.GenericIPAddressField()


class PostTag(models.Model):
    tagged_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_text
