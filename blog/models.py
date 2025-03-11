from django.db import models
from django.contrib.auth.models import User


#title,slug

class Category(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100,unique=True,allow_unicode=True,verbose_name='نامک')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        
    def __str__(self):
        return self.title
    

    
class Tag(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='عنوان برچسب')
    slug = models.SlugField(max_length=100,unique=True,allow_unicode=True,verbose_name='نامک')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'
    
    def __str__(self):
        return self.title
    

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده مقاله')
    category = models.ManyToManyField(Category,related_name='articles',verbose_name='انتخاب دسته بندی')
    tags = models.ManyToManyField(Tag,related_name='tags',verbose_name='انتخاب برچسب',null=True,blank=True)
    title = models.CharField(max_length=100,unique=True, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100,unique=True,allow_unicode=True,verbose_name='نامک')
    description = models.TextField(verbose_name='محتوای مقاله')
    image = models.ImageField(upload_to='articles/',verbose_name='بنر مقاله')
    status = models.BooleanField(default=False,verbose_name='منتشر شود؟')
    views = models.IntegerField(default=0,verbose_name='بازدید')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True,verbose_name='تاریخ بروزرسانی')
    
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
    
    def __str__(self):
        return self.title
    
    
    