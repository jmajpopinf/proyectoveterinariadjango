from django.urls import path
from home import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.home_index), name='home_index')
]
