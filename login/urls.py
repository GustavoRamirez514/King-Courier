from django.urls import path
from . import views
from user.views import edit_profile

urlpatterns = [
    path('', views.login_home, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.log_out, name='logout'),
    path('perfil/edit', edit_profile, name='editar_perfil'),
]
