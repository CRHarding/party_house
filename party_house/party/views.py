from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Party, PartyInformation, Testimonial

def index(request):
        return render(
        request,
        'index.html',
        context=
        {
      
        }
    )
