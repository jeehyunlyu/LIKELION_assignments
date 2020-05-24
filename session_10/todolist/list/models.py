from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    duedate = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()