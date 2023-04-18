from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('',MenHome.as_view(), name = 'home'),
    path('about/', about, name='about'),
    path('addproduct/',AddProduct.as_view(), name= 'add_product'),
    path('contact/',contact, name='contact'),
    path('product/',product, name= 'product'),
    path('qyzmet/',qyzmet, name= 'qyzmet'),
    path('registration/',registration, name= 'registration'),
    path('login/',login, name= 'login'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name = 'post'),
    path('category/<slug:cat_slug>/',MenCategory.as_view(),name = 'category'),
    path('zhalga',renting,name = 'renting'),
    path('satu',satu,name = 'satu')


]