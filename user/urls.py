from django.urls import path
from user.views import RegistrarUsuario

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='registrar')
]