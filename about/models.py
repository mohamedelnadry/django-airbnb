from django.db import models
from django.urls import reverse

# Create your models here.

class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_gouls = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='about/')


    

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class FAQ(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    

    class Meta:
        verbose_name = ("FAQ")
        verbose_name_plural = ("FAQ")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("FAQ_detail", kwargs={"pk": self.pk})
class INFO(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company/')
    description = models.TextField(max_length=500)
    fb_url = models.URLField(max_length=200,null=True,blank=True)
    twitter_url = models.URLField(max_length=200,null=True,blank=True)
    instgram_url = models.URLField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)


    

    class Meta:
        verbose_name = ("INFO")
        verbose_name_plural = ("INFO")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("INFO_detail", kwargs={"pk": self.pk})
