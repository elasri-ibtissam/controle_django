from django.contrib import admin
from .models import Modele,Vehicule,Reservation
# Register your models here.

class AdminModel(admin.ModelAdmin):
    list_display = ('nom_model', 'date_sortie')

class AdminVehicule(admin.ModelAdmin):
    list_display  = ('carburant', 'kilometrage' ,'prix' ,'modele' ,'date_ajout')
admin.site.register(Vehicule, AdminVehicule)
admin.site.register(Modele, AdminModel)
admin.site.register(Reservation)