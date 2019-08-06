from django.db import models

# Create your models here.

class Teacher(models.Model):
    nickname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    specialty = models.CharField(max_length=200)
    residence = models.CharField(max_length=100)
    references = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.nickname