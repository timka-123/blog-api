from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    full_post = models.TextField()
    author = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
