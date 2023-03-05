from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('',index, name = 'home'),
    path('about/', about, name='about'),
    path('addproduct/',addproduct, name= 'add_product'),
    path('contact/',contact, name='contact'),
    path('product/',product, name= 'product'),
    path('qyzmet/',qyzmet, name= 'qyzmet'),
    path('registration/',registration, name= 'registration'),
    path('login/',login, name= 'login'),
    path('post/<slug:post_slug>/',show_post,name = 'post'),
    path('category/<int:cat_id>/',show_category,name = 'category'),
    path('zhalga',renting,name = 'renting'),
    path('satu',satu,name = 'satu')


]