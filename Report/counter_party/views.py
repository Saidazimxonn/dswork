from django.db import models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import CounterParty

class CounterPartyView(TemplateView):
    template_name = 'con_party_list.html'
    def get_context_data(self, **kwargs):
        context = super(CounterPartyView, self).get_context_data(**kwargs)
        return context
    
class CounterPartyListView(ListView):
    template_name = 'con_party_list.html'
    model = CounterParty
    
    def get_context_data(self, **kwargs):
        context = super(CounterPartyListView, self).get_context_data(**kwargs)
        context['conpartylist'] = CounterParty.objects.all().order_by('-id')
        return context

class CounterPartyCreateView(CreateView):
    template_name =  'con_party_creat.html'
    model  = CounterParty
    fields = '__all__'
    success_url = '/con-party/'


    
class CounterPartyUpdate(UpdateView):
    template_name = 'con_party_update.html'
    model = CounterParty
    fields = '__all__'
    success_url = '/con-party/'