from django.urls import path
from . import views

urlpatterns = [
    path('/inscription/',views.Inscription, name='inscription' ),
    path('/login/',views.Login,name='login'),
    path('/quitter/', views.LogoutUser, name='quitter')

]