from django.db import models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import Delivery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class DeliveryView(TemplateView):
    template_name = 'deliver_list.html'
    def get_context_data(self, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        return context

class DeliveryListView(ListView):
    template_name = 'deliver_list.html'
    model = Delivery
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super(DeliveryListView, self).get_context_data(**kwargs)
        deliverys = Delivery.objects.all().order_by('-id')
        paginator = Paginator(deliverys, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
             
        context['deliverys'] = file_exams
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


    