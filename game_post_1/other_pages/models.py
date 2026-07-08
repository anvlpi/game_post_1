from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    surname = models.CharField(max_length=128, blank=False, null=False)
    position_eng = models.CharField(max_length=128)
    position_ru = models.CharField(max_length=128)
    position_description = models.CharField(max_length=256)
    link_vk = models.URLField(max_length=500)
    link_tg = models.URLField(max_length=500)
    link_mail = models.URLField(max_length=500)
    photo = models.ImageField(upload_to='avatars/')
    active = models.BooleanField(default=True)
