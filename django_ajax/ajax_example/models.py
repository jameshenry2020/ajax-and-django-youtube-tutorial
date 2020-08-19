from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=60)
    post=models.TextField()
    author=models.CharField(max_length=50)

    def __str__(self):
        return self.title