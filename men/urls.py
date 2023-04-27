from django.urls import path, re_path

from .views import *
# from django.views.decarator.cache import cache_page

urlpatterns = [
    path('',MenHome.as_view(), name = 'home'),
    path('api/v1/menlist/', MenApiView.as_view()),
    path('about/', about, name='about'),
    path('addproduct/',AddProduct.as_view(), name= 'add_product'),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('product/',product, name= 'product'),
    path('qyzmet/',qyzmet, name= 'qyzmet'),
    path('registration/',RegisterUser.as_view(), name= 'registration'),
    path('login/',LoginUser.as_view(), name= 'login'),
    path('logout/',logout_user, name = 'logout'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name = 'post'),
    path('category/<slug:cat_slug>/',MenCategory.as_view(),name = 'category'),
    path('zhalga',renting,name = 'renting'),
    path('satu',satu,name = 'satu')


]