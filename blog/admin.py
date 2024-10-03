from django.contrib import admin
from blog.models import Tag, Post


admin.site.register(Tag)
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')


admin.site.register(Post, PostAdmin)