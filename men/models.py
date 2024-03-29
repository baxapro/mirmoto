from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Men(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    slug = models.SlugField(max_length = 255,unique = True,db_index=True,verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = True)
    cat = models.ForeignKey('Category', on_delete = models.PROTECT)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь',on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={ 'post_slug':self.slug })


    class Meta:
        verbose_name = 'Moto'
        verbose_name_plural = 'Moto'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index = True)
    slug = models.SlugField(max_length = 255,unique = True,db_index=True,verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug':self.slug})

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

class Thing(models.Model):
    name = models.CharField(max_length=100, db_index = True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thing', kwargs={'thing_id':self.pk})



