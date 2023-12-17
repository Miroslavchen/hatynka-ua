from django.db import models
from django.db.models import *
from django.urls import reverse


class Status(models.Model):
    Name = CharField("Name", max_length=250)
    url = CharField("url", max_length=50, unique=True, db_index=True)
    X = CharField("X", max_length=20)
    Y = CharField("Y", max_length=20)
    Z = CharField("Z", max_length=20)
    Time = DateTimeField("Time", max_length=15)
    Cost = CharField("Cost", max_length=20)
    Img1 = ImageField("Img1", upload_to='photos/%Y/%m/%d')
    Img2 = ImageField("Img2", upload_to='photos/%Y/%m/%d', blank=True)
    Img3 = ImageField("Img3", upload_to='photos/%Y/%m/%d', blank=True)
    Img4 = ImageField("Img4", upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.Name

    def get_absolutle_url(self):
        return reverse('post', kwargs={'post_url': self.url})

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Види"

class Buy(models.Model):
    idi = IntegerField('id', unique=True, db_index=True, auto_created=True, primary_key=True)
    Name = CharField("Name", max_length=250)
    Phone = CharField("Phone", max_length=16)
    url = CharField("url", max_length=50)
    Email = EmailField("Email", max_length=255)

    def __str__(self):
        return self.Name

    def get_absolutle_url(self):
        return reverse('zam', kwargs={'zam_id': self.idi})

    class Meta:
        verbose_name = "Покупку"
        verbose_name_plural = "Покупки"
