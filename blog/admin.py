from django.contrib import admin
from .models import Post,Comment

#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin): #For admin panel allow you to filter, search etc.
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status','publish']
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
# Register your models here.
