from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Party, PartyInformation, Testimonial, User
from django.views import generic

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
    template_name = '/profile'
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
