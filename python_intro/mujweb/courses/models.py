from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Ucitel jmenem {self.name} ma ID {self.pk}"

class Course(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
