from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.PartyListView.as_view(), name='party-list-view'),
    path('party-details/<int:pk>', views.PartyDetailView.as_view(), name='party-information-detail'),
    path('RSVP/<int:user_id>/<str:creator>/<int:id>', views.PartyRSVPView),
]

from django.contrib.auth.decorators import login_required

urlpatterns += [
    path('party/create/', login_required(views.PartyCreate.as_view()), name='party_create'),
]
