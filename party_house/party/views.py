from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Party, PartyInformation, Testimonial

def index(request):
    all_parties = PartyInformation.objects.filter(party__active = 'True')

    
    return render(
        request,
        'index.html',
        context=
        {
            'all_parties':all_parties,
        }
    )

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PartyInformation

class PartyCreate(CreateView):
    model = PartyInformation
    fields = '__all__'