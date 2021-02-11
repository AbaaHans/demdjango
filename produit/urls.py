from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('Liste_des_produits',views.List_Pds,name="Liste_des_produits"),
    path('modif_prod/<str:pk>', views.Modifier_Pdts, name='modif_prod'),
    path('suppr_prod/<str:pk>', views.Supprimer_Pdts, name='suppr_prod'),
    path('/ajoute_prod', views.Ajout_Prod, name='ajoute_prod')

]
