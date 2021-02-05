
from django.shortcuts import render,redirect
from .forms import CommandeForm
from .models import Commande

def List_Cmd(request):
    return render(request,'commande/listecommande.html')

def Ajouter_Cmd(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    cotext={'form':form}
    return render(request,'commande/ajouter_commande.html',cotext)

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

def Supprimer_Cmd(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'commande/supprimer.html',context)