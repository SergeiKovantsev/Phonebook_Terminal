from django.db import models

class Entry(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    personal_phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

