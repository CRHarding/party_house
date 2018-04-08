from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.contrib.auth.decorators import login_required

urlpatterns += [  
    path('party/create/', login_required(views.PartyCreate.as_view()), name='party_create'),
]
