from django.urls import path
from . import views
from user.views import eliminar_usuario

urlpatterns = [
    path('users/', views.users_list, name='users'),
    path('users/register/', views.user_create, name='register'),
    path('users/user/<int:user_id>/eliminar/', eliminar_usuario, name='eliminar_usuario'),
]   