from django.core import paginator
from django.db import models
from django.db.models import fields
from django.views.generic import  CreateView ,ListView
from django.views.generic.base import TemplateView
from payment.models import Payment
from counter_party.models import CounterParty
from delivery.models import Delivery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class FilterView(TemplateView):
    template_name = 'filter_pay.html'
    paments = Payment.objects.all().order_by('-id')
    
    
    def get_context_data(self, **kwargs):
        counter = []
        context = super(FilterView, self).get_context_data(**kwargs)
        startdate = self.request.GET.get('startdate', None)
        enddate = self.request.GET.get('enddate', None)
        counterpary = self.request.GET.get('counterparty', 'all')
        delivery = self.request.GET.get('delivery', 'all')

        paments = Payment.objects.all().order_by('-id')
       
        if startdate and enddate:
            paments = paments.filter(created__range=[startdate + " 00:00", enddate + " 23:59"])
        if counterpary != 'all':
            paments = paments.filter(counter_party_id=int(counterpary))
        if delivery != 'all':
            paments = paments.filter(delivery_id=int(delivery))


             
        context['filters'] = paments
        context['counter_parties'] = CounterParty.objects.all()
        context['deliverys'] = Delivery.objects.all()
        context['startdate'] = startdate
        context['enddate'] = enddate
        context['selected_counter_pary'] = counterpary
        context['selected_deliverys'] = delivery

        return context

    def get_queryset(self):
        startdate = self.request.GET.get('startdate', None)
        enddate = self.request.GET.get('enddate', None)
        

class FilterCreate(CreateView):
    template_name = 'filter_pay.html'
    models = Payment
    fields = ['counterparty']
