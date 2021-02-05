from django.shortcuts import render
from commande.models import Commande
from client.models import Client

def home(request):
    commandes= Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/home.html',context)
