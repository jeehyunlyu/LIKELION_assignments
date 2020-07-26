from django.contrib import admin
from .models import ToDo, Comment, Like, Bookmark

# Register your models here.
admin.site.register(ToDo)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Bookmark)