from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'slug', 'modified']
    search_fields = ('title', 'slug')
    list_filter = ('modified',)
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('user', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'is_reply', 'created']
    raw_id_fields = ['user', 'post', 'reply']


admin.site.register(Like)
