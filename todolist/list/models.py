from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    duedate = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    img = models.TextField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content
