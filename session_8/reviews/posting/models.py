from django.db import models

# Create your models here.
class Review(models.Model):

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    content = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title