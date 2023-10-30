from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.CharField( max_length=100, unique=True )
    short_code = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.short_code