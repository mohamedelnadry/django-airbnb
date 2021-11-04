from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='owner_vlog', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=15000)
    created_at = models.DateTimeField(default=timezone.now)
    imge = models.ImageField(upload_to='blog/')
    category = models.ForeignKey("Category", related_name='Category_blog', on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(null=True,blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_absolute_url(self):
        return reverse("BlogDetails", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        elif self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    
    


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name