from django.db import models

# Create your models here.

class Tag(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200,null=True)
    prix = models.FloatField(null=True)
    image_url = models.ImageField(null=True,blank=True)

    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom