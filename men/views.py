from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render , redirect, get_object_or_404
from django.views.generic import ListView,DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .utils import *
from .models import *
# Create your views here.




class MenHome(DataMixin,ListView):
    paginete_by = 3
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))
    def get_queryset(self):
        return Men.objects.filter(is_published=True)

# def index(request):
#     posts = Men.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'regis':regis,
#         'title': 'Index page',
#         'cat_selected': 0,
#     }
#     return render(request, 'men/index.html',context = context)

def about(request):
    return render(request, 'men/about.html',{'menu': menu,'title':'About page'})


class AddProduct(LoginRequiredMixin,DataMixin,CreateView):
    form_class = AddProductForm
    template_name = 'men/addProduct.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='ADD product')
        return dict(list(context.items())+list(c_def.items()))


# def addproduct(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddProductForm()
#     return render(request, 'men/addProduct.html',{'form':form,'menu':menu,'title':'Add Product'})

def product(request):
    things = Thing.objects.all()
    context = {
        'things': things,
        'menu': menu,
        'regis':regis,
        'title': 'Thing page',

    }

    return render(request, 'men/thing.html', context=context)

def contact(request):
    return HttpResponse('Contact')

def qyzmet(request):
    return HttpResponse('Qyzmet')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'men/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))

def login(request):
    return HttpResponse('Login')


class ShowPost(DataMixin,DetailView):
    model = Men
    template_name= 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))

# def show_post(request,post_slug):
#     post = get_object_or_404(Men, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request,'men/post.html', context=context)

class MenCategory(DataMixin,ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def=self.get_user_context(title='Category - '+str(context['posts'][0].cat),
                                    cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items())+list(c_def.items()))


    def get_queryset(self):
        return Men.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published = True)

# def show_category(request,cat_id):
#     posts = Men.objects.filter(cat_id=cat_id)
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'regis': regis,
#         'title': 'Category',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'men/index.html', context=context)

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



