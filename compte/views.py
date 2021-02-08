from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CreeUtilisateur

# Create your views here.

def Inscription(request):
    form = CreeUtilisateur()
    if request.method=='POST':
        form=CreeUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data('username')
            messages.success(request,'Compte créer avec succès')
            return redirect('login')
    context = {'form':form}
    return render(request,'compte/inscription.html',context)


def Login(request):
    context= {}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Identifiant/Mot de passe incorrect')
    return render(request,'compte/login.html',context)