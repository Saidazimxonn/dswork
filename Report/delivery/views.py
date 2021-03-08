from django.db import models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import Delivery

class DeliveryView(TemplateView):
    template_name = 'deliver_list.html'
    def get_context_data(self, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        return context

class DeliveryListView(ListView):
    template_name = 'deliver_list.html'
    model = Delivery
    
    def get_context_data(self, **kwargs):
        context = super(DeliveryListView, self).get_context_data(**kwargs)
        context['deliverys'] = Delivery.objects.all().order_by('-id')
        context['salom'] = 'Sasasasasas'
        return context

class DeliverCreateView(CreateView):
    template_name = 'deliver_created.html'
    model = Delivery
    fields = '__all__'
    success_url = '/delivery/'

class DeliverUpdateView(UpdateView):
    template_name = 'deliver_update.html'
    model = Delivery
    fields = '__all__'
    success_url = '/delivery/'


    