from django.db import models

# Create your models here.


class GuestList(models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    message = models.TextField(max_length=1000)
    image = models.FileField()

    def __str__(self):
        return self.title