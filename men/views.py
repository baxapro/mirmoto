from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render , redirect, get_object_or_404

from .forms import *
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
    context = {
        'posts': posts,
        'menu': menu,
        'regis':regis,
        'title': 'Index page',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html',context = context)

def about(request):
    return render(request, 'men/about.html',{'menu': menu,'title':'About page'})

def addproduct(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddProductForm()
    return render(request, 'men/addProduct.html',{'form':form,'menu':menu,'title':'Add Product'})

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


def show_post(request,post_slug):
    post = get_object_or_404(Men, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request,'men/post.html', context=context)

def show_category(request,cat_id):
    posts = Men.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'menu': menu,
        'regis': regis,
        'title': 'Category',
        'cat_selected': cat_id,
    }
    return render(request, 'men/index.html', context=context)

def satu(request):
    posts = Men.objects.filter(cat_id=2)
    context = {
        'posts': posts,
        'menu': menu,
        'regis': regis,
        'title': 'Category',
        'cat_selected': 2,
    }
    return render(request, 'men/satu.html', context=context)

def renting(request):
    posts = Men.objects.filter(cat_id=1)
    context = {
        'posts': posts,
        'menu': menu,
        'regis': regis,
        'title': 'Category',
        'cat_selected': 2,
    }
    return render(request, 'men/zhalga.html', context=context)























def pageNotFound(request,exception):
    return render(request,'men/404.html')

def Error(request,exception):
    return render(request,'men/403.html')

def Error400(request,excepion):
    return render(request,'men/400.html')



