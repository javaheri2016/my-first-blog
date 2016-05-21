from django.db import models
from django.utils import timezone

#from i import importuje elementy z innych plikow

#nazwa modelu wielka litera
#class sygnalizuje, ze tworzymy obiekt

class Post(models.Model):
    author = models.ForeignKey('auth.User') #ForeignKey odnosnik do innego modelu
    title = models.CharField(max_length=200) #CharField - tekst z ograniczona liczba znakow
    text = models.TextField() #bez ograniczen znakow
    created_date = models.DateTimeField(
            default=timezone.now) 
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
