from django.forms import ModelForm
from .models import Produit
from django import forms

class ProduitForm(ModelForm):
    class Meta:
        model=Produit
        fields='__all__'

