from django.urls import path
from voiture.views import index, detail, liste,confirmer, login,register

urlpatterns = [
    path('',login,name='home'),
    path('index',index,name="index"),
    path('<int:myid>', detail, name="detail"),
    path('liste',liste,name="liste"),
    path('confirmer',confirmer, name="confirmer"),
    path('login',login,name="login"),
    path('register',register,name="register")
  

] 