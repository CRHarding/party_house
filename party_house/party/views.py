from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Party, PartyInformation, Testimonial

def index(request):
    # all_parties_information = PartyInformation.objects.get()
    # active_parties = all_parties_information.entry_set.all()
    # active_parties.filter(active__exact('True'))

    return render(
        request,
        'index.html',
        context=
        {
        # 'all_parties_information':all_parties_information,
        }
    )
