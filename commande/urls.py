from django.urls import path
from . import views

urlpatterns = [
    path('',views.List_Cmd, name='listecommande' ),
    path('ajout_cmd/',views.Ajouter_Cmd, name='ajout_cmd'),
    path('modif_cmd/<str:pk>', views.Modifier_Cmd, name='modif_cmd'),
    path('suppr_cmd/<str:pk>', views.Supprimer_Cmd, name='suppr_cmd')

]
