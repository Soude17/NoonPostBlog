from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','created']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']

    
 
@admin.register(models.Tag)    
class TagAdmin(admin.ModelAdmin):
    list_display = ['title','created']
    prepopulated_fields ={'slug':('title',)}
    search_fields = ['title']
    

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author','title','views','status','created']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']
    list_filter = ['status']
    list_editable = ['status']
    