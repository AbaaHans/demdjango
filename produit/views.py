from django.shortcuts import render,redirect
from commande.models import Commande
from client.models import Client
from produit.models import Produit
from .forms import ProduitForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    commandes= Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/home.html',context)

@login_required(login_url='login')
def List_Pds(requets):
    produits=Produit.objects.all()
    context={'produits':produits}
    return  render(requets,'produit/listproduit.html',context)


@login_required(login_url='login')
def Ajout_Prod(request):
    form=ProduitForm()
    if request.method=='POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Liste_des_produits')
    context={'form':form}
    return render(request,'produit/ajouterproduit.html',context)

@login_required(login_url='login')
def Supprimer_Pdts(request,pk):
    produit=Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('Liste_des_produits')
    context={'item':produit}
    return render(request,'produit/supprimer.html',context)


@login_required(login_url='login')
def Modifier_Pdts(request,pk):
    produit=Produit.objects.get(id=pk)
    form=ProduitForm(instance=produit)
    if request.method=='POST':
        form=ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('/Liste_des_produits')
    context={'form':form}
    return render(request,'produit/modifier.html',context)


