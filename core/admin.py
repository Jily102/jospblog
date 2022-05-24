from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'descript', 'content', 'author']

admin.site.register(Post, PostAdmin)