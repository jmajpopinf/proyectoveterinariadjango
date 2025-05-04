from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from user.forms import RegistroForm

# Create your views here.
class RegistrarUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuario/registrar.html'
    success_url = reverse_lazy('login')