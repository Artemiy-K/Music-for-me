from django.contrib import admin
from .models import Music

class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','like' ,'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
# Register your models here.


admin.site.register(Music, MusicAdmin)
