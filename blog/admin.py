from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ('author',)
    date_hierachy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)


# Register your models here.
