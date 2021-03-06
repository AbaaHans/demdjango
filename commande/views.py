
from django.shortcuts import render,redirect
from .forms import CommandeForm
from .models import Commande
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def List_Cmd(request):
    Commandes=Commande.objects.all()
    context={'commandes':Commandes}
    return render(request,'commande/listecommande.html',context)

@login_required(login_url='login')
def Ajouter_Cmd(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    cotext={'form':form}
    return render(request,'commande/ajouter_commande.html',cotext)

@login_required(login_url='login')
def Modifier_Cmd(request,pk):
    commande=Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    cotext={'form':form}
    return render(request,'commande/ajouter_commande.html',cotext)

@login_required(login_url='login')
def Supprimer_Cmd(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'commande/supprimer.html',context)