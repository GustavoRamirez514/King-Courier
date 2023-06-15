from django.urls import path
from . import views
from user.views import eliminar_usuario

urlpatterns = [
    path('', views.users_list, name='users'),
    path('register/', views.user_create, name='register'),
    path('user/<int:user_id>/eliminar/', eliminar_usuario, name='eliminar_usuario'),
]   