from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    title = ':)'
    return render(request,'about.html',{ 'title' : title})


