from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [  
    path('party/create/', views.PartyCreate.as_view(), name='party_create'),
]
