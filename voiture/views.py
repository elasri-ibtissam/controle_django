from turtle import home
from django.shortcuts import redirect  
from django.shortcuts import render
from .models import Vehicule, Reservation
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.
def index(request):
    vehicule_object = Vehicule.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        vehicule_object = Vehicule.objects.filter(carburant__icontains=item_name)
    paginator = Paginator(vehicule_object, 4)
    page = request.GET.get('page')
    vehicule_object = paginator.get_page(page)

    return render(request, 'voiture/index.html', {'vehicule_object':vehicule_object})

def detail(request, myid):
    vehicule_object = Vehicule.objects.get(id=myid)
    return render(request, 'voiture/detail.html',{'vehicule':vehicule_object} )

def liste(request):
    if request.method =="POST":
        model_vehicule = request.POST.get('model_vehicule')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        date_depart = request.POST.get('date_depart')
        date_retour = request.POST.get('date_retour')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        res = Reservation(model_vehicule=model_vehicule,nom=nom, prenom=prenom, email=email, telephone=telephone, date_depart=date_depart, date_retour=date_retour, adresse=adresse, ville=ville)
        res.save()
        return redirect('confirmer')


    return render(request, 'voiture/liste.html')

def confirmer(request):
    info = Reservation.objects.all()[:1]
    for item in info:
        nom= item.nom
    return render(request, 'voiture/confirmer.html',{'name': nom})




def login(request):
       if request.method =="POST":
        eml = request.POST.get('eml')
        password1 = request.POST.get('password')
        print(eml,password1)
        user=authenticate(request,eml=eml,password=password1)
       
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("rr")
        
       else:
            return render(request, 'voiture/login.html',{})

def register(request):
      if request.method =="POST":
          emle = request.POST.get('emle')
          password1 = request.POST.get('password1')
          password2 = request.POST.get('password2')

          if password1!=password2:
              return HttpResponse("erreur")

         
          my_user=User.objects.create_user(emle,password1,password2)
          my_user.save()
          return redirect('login')


          print(emle,password1,password2)


          

      return render(request,'voiture/register.html')
        