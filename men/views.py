from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render , redirect
from .models import *

# Create your views here.

menu = ['Home','About me','categories']

def index(request):
    posts = Men.objects.all()
    return render(request, 'men/index.html', {'posts':posts,'menu': menu,'title':'Index page'})

def about(request):
    return render(request, 'men/about.html',{'menu': menu,'title':'About page'})


def categories(request, catid):
    # if request.POST:
    #    print(request.POST)

    return HttpResponse(f"<img src='https://www.unisender.com/wp-content/uploads/2020/11/01-2-768x346.png' ><p>{catid}</p>")

def archive(request,year):
    if int(year)>2020:
        return redirect('home')
    return HttpResponse(f"<h1>History {year}</h1>")

def pageNotFound(request,exception):
    return render(request,'men/404.html')

def Error(request,exception):
    return render(request,'men/403.html')

def Error400(request,excepion):
    return render(request,'men/400.html')

