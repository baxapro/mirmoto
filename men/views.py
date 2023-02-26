from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render , redirect
from .models import *

# Create your views here.

menu = [{'title': 'Басты бет','url_name': 'home'},
        {'title': 'Біз туралы','url_name': 'about'},
        {'title': 'Мопед қосу','url_name': 'add_product'},
        {'title': 'Қызметтер','url_name': 'qyzmet'},
        {'title': 'Заттар', 'url_name': 'product'},
        {'title': 'Байланыс', 'url_name': 'contact'}

        ]
regis = [{'title':'Тіркелу','url_name':'registration'},
         {'title':'Кіру','url_name':'login'}
         ]

def index(request):
    posts = Men.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'cats':cats,
        'regis':regis,
        'title': 'Index page',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html',context = context)

def about(request):
    return render(request, 'men/about.html',{'menu': menu,'title':'About page'})

def addproduct(request):
    return HttpResponse('Add Product')

def product(request):
    return HttpResponse('Product')

def contact(request):
    return HttpResponse('Contact')

def qyzmet(request):
    return HttpResponse('Qyzmet')

def registration(request):
    return HttpResponse('Registration')

def login(request):
    return HttpResponse('Login')


def show_post(request,post_id):
    return HttpResponse(f"Id={post_id}")

def show_category(request,cat_id):
    return HttpResponse(f"Id={cat_id}")

def pageNotFound(request,exception):
    return render(request,'men/404.html')

def Error(request,exception):
    return render(request,'men/403.html')

def Error400(request,excepion):
    return render(request,'men/400.html')



