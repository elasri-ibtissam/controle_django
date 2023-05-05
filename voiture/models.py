from django.db import models

# Create your models here.

class Modele(models.Model):
    nom_model = models.CharField(max_length=200)
    date_sortie = models.DateTimeField(auto_now=True)

  
    def __str__(self) :
        return self.nom_model


class Vehicule(models.Model):
    carburant = models.CharField(max_length=200)
    kilometrage = models.IntegerField()
    prix = models.FloatField()
    modele = models.ForeignKey(Modele, related_name='lemodele', on_delete=models.CASCADE)
    nbr_place = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=5000)
    date_ajout = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.carburant
    

class Reservation(models.Model):
    model_vehicule = models.CharField(max_length=200,null=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=200)
    date_depart =models.DateTimeField()
    date_retour = models.DateTimeField()
    adresse= models.CharField(max_length=200,null=True)
    ville = models.CharField(max_length=200,null=True)


    def __str__(self) :
        return self.nom


    