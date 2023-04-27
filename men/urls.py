from django.urls import path, re_path,include
from django.contrib import admin
from rest_framework import routers
from men.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get':'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix':'list'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]
# from django.views.decarator.cache import cache_page
# router = MyCustomRouter()
# router.register(r'men',MenViewSet,basename='men')
# print(router.urls)

urlpatterns = [
    path('',MenHome.as_view(), name = 'home'),
    path('admin/',admin.site.urls),
    # path('api/v1/',MenAPIList.as_view()),
    path('api/v1/men/', MenAPIList.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/men/<int:pk>/', MenAPIUpdate.as_view()),
    path('api/v1/mendelete/<int:pk>/', MenAPIDestroy.as_view()),
    path('api/v1/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/v1/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/v1/token/verify/',TokenVerifyView.as_view(),name='token_verify'),
    path('about/', about, name='about'),
    path('addproduct/',AddProduct.as_view(), name= 'add_product'),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('product/',product, name= 'product'),
    path('registration/',RegisterUser.as_view(), name= 'registration'),
    path('login/',LoginUser.as_view(), name= 'login'),
    path('logout/',logout_user, name = 'logout'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name = 'post'),
    path('category/<slug:cat_slug>/',MenCategory.as_view(),name = 'category'),
    path('zhalga',renting,name = 'renting'),
    path('satu',satu,name = 'satu')


]