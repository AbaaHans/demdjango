from django.urls import path
from . import views

urlpatterns = [
    path('/<str:pk>',views.List_Clts, name='client' ),
    path('ajout_clt',views.Ajouter_Clts, name='ajout_clt'),
    path('suppr_clts/<str:pk>',views.Supprimer_Clts, name='suppr_clts'),
    path('All_Clts',views.All_Clts,name="All_Clts")
]
