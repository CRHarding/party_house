from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.PartyListView.as_view(), name='party-list-view')
]
