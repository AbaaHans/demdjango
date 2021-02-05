from django.shortcuts import render
from commande.models import Commande
from client.models import Client
def List_Clts(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    context={'client':client,'commande':commande,'commande_total':commande_total}
    return render(request,'client/listclient.html',context)


def Ajouter_Clts(request):
    return render(request,'client/ajouter_client.html')


def Supprimer_Clts(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
    context={'item':commande}
    return render(request,'commande/supprimer.html',context)