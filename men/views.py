from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.forms import model_to_dict
from rest_framework import generics,viewsets,mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import MenSerializer
from .utils import *
from .models import *



# Create your views here.

class MenAPIListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000
class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MenAPIListPagination


class MenAPIUpdate(generics.UpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly, )


class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
class MenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Men.objects.all()[:3]
        return Men.objects.filter(pk=pk)
    @action(methods=['get'],detail=True)
    def category(self,request,pk=None):
        cats=Category.objects.get(pk=pk)
        return Response({'cats': cats.name})



    # class MenApiView(APIView):
    #     def get(self, request):
    #         w = Men.objects.all()
    #         return Response({'posts':MenSerializer(w, many=True).data})
    #
    #     def post(self, request):
    #
    #         serializer = MenSerializer(data = request.data)
    #         serializer.is_valid(raise_exeption = True)
    #         serializer.save()
    # post_new = Men.objects.create(
    #     title=request.data['title'],
    #     content = request.data['content'],
    #     cat_id = request.data['cat_id'],
    #     content1 = request.data['content1'],
    #     content2 = request.data['content2']
    # )
    # return Response({'post': MenSerializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Error": "Put method not allowed"})
        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({"Error": "Put method not allowed"})
        serializer = MenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        return Response({"Post": serializer.data})


# class MenApiView(generics.ListAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
class MenHome(DataMixin, ListView):
    paginete_by = 3
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

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
    return render(request, 'men/about.html', {'menu': menu, 'title': 'About page'})


class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'men/addProduct.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='ADD product')
        return dict(list(context.items()) + list(c_def.items()))


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
        'regis': regis,
        'title': 'Thing page',

    }

    return render(request, 'men/thing.html', context=context)


#
# def contact(request):
#     return HttpResponse('Contact')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'men/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'men/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'men/login.html'

    def get_context_date(self, *, object_list=None, **kwargs):
        context = super().get_context_date(**kwargs)
        c_def = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ShowPost(DataMixin, DetailView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


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

class MenCategory(DataMixin, ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Men.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


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


def pageNotFound(request, exception):
    return render(request, 'men/404.html')


def Error(request, exception):
    return render(request, 'men/403.html')


def Error400(request, excepion):
    return render(request, 'men/400.html')
