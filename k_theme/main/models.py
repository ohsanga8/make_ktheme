from django.db import models


# Create your models here.
class KthemeImage(models.Model):
    image1 = models.ImageField(null="True", upload_to="images/", blank="True")


def __str__(self):
    return str(self.title)
