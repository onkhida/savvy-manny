from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','publish','status') 
    list_filter = ('publish','created','updated')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('author',)
    raw_id_fields = ('author',)

