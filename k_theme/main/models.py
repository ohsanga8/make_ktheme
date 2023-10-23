from django.db import models


# Create your models here.
class Ktheme(models.Model):
    theme_id = models.CharField(max_length=50)
    theme_name = models.CharField(max_length=50)
    dir_path = models.CharField(max_length=100)
