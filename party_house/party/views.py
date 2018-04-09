from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Party, PartyInformation, Testimonial
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    all_parties = PartyInformation.objects.filter(active = 'True')

    return render(
        request,
        'index.html',
        context=
        {
            'all_parties':all_parties,
        }
    )

class PartyListView(generic.ListView):
    model = User
    context_object_name = 'my_party_list'
    queryset = PartyInformation.objects.all()
    template_name = '/partyinformation_list'
    def get_context_data(self, **kwargs):
        context = super(PartyListView, self).get_context_data(**kwargs)
        context['thumbs'] = User.objects.filter(attended__user = self.request.user)
        context['your_active_going_parties'] = PartyInformation.objects.filter(active = 'True').filter(party__status = 2).filter(party__party_goer_id = self.request.user.id)
        context['your_old_going_parties'] = PartyInformation.objects.filter(active = 'False').filter(party__status = 2).filter(party__party_goer_id = self.request.user.id)
        context['your_active_created_parties'] = PartyInformation.objects.filter(active = 'True').filter(party__party_thrower_id = self.request.user.id)
        context['your_old_created_parties'] = PartyInformation.objects.filter(active = 'False').filter(party__party_thrower_id = self.request.user.id)
        context['your_active_pending_parties'] = PartyInformation.objects.filter(active = 'True').filter(party__status = 1).filter(party__party_goer_id = self.request.user.id)
        context['your_active_rejected_parties'] = PartyInformation.objects.filter(active = 'False').filter(party__status = 3).filter(party__party_goer_id = self.request.user.id)
        context['your_active_parties_attended'] = PartyInformation.objects.filter(active = 'True').filter(party__status = 2).filter(party__party_goer_id = self.request.user.id).filter(party__attended = True)
        context['your_old_parties_attended'] = PartyInformation.objects.filter(active = 'False').filter(party__party_goer_id = self.request.user.id).filter(party__status = 2).filter(party__attended = True)
        context['your_old_parties_not_attended'] = PartyInformation.objects.filter(active = 'False').filter(party__party_goer_id = self.request.user.id).filter(party__status = 2).filter(party__attended = False)
        return context

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PartyInformation

class PartyCreate(generic.CreateView):
    model = PartyInformation
    fields = [
    'address_st', 'address_num', 'address_apt_num', 'address_zip', 'address_city', 'description', 'date_of_party', 'creator', 'active']
    success_url = reverse_lazy('index')

from django.views import generic

class PartyDetailView(generic.DetailView):
    model = PartyInformation
    template_name = 'party/partyinformation_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartyDetailView, self).get_context_data(**kwargs)
        context['party_thrower_id'] = PartyInformation.creator
        context['party_information_id'] = PartyInformation.id
        return context

def PartyRSVPView(request, user_id=1, creator=1, id=1):
    # user_id = request.GET.get('user_id')
    # creator = request.GET.get('creator')
    # id = request.GET.get('id')
    # user_id = int(user_id)
    # creator = int(creator)
    # id = int(id)
    party = Party()
    Party.objects.create(party_information_id=id, party_thrower_id=creator, party_goer_id=user_id)

    return render(request, 'party')
