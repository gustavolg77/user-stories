from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def about(request):
    title = ':)'
    return render(request,'about.html',{ 'title' : title})

def verificarUsuario(request):
    usuarios = Usuario.objects.all()
    return render(request,'login.html',{'usuarios':usuarios}) #usuarios [{},{},{}]
