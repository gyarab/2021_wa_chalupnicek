from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    csfd_rating = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey('Director', null=True, blank=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', blank=True)
    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.title

SEX_MALE = 'male'
SEX_FEMALE = 'female'
SEX_OTHER = 'other'

SEX_CHOICES = (
    (SEX_MALE, 'Muž'),
    (SEX_FEMALE, 'Žena'),
    (SEX_OTHER, 'Ostatní'),
)

class Actor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True) 
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=32, default=SEX_MALE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Director(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
