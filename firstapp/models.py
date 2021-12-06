from django.db import models


# Create your models here.
class people(models.Model):
    username = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)
    password = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=11)

    def _str_(self):
        return self.name


class article(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True, )
    img = models.ImageField(upload_to='images', default='')

    def _str_(self):
        return self.headline
