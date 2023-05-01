from django.urls import path
from . import views as views_login
from user import views as views_user

urlpatterns = [
    path('', views_login.login_home, name='login'),
    path('users/', views_user.users_list, name='users'),
    path('perfil/', views_login.perfil, name='perfil'),
    path('register/', views_login.user_create, name='register'),
    path('logout/', views_login.log_out, name='logout'),
]
