from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Article(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE,verbose_name = "author name")
    title = models.CharField(max_length = 100,verbose_name = "title")
    content = models.TextField(verbose_name='content')
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']



