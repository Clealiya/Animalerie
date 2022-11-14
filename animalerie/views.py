from django.shortcuts import render
from .models import Equipement, Animal

def accueil(request):
    animaux = Animal.objects.all().order_by('id_animal')
    equipements = Equipement.objects.all().order_by('id_equip')
    return render(request, 'animalerie/accueil.html', {'animaux': animaux, 'equipements': equipements})

    