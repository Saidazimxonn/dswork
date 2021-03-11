from django.shortcuts import redirect
from counter_party.models import CounterParty
from django.db.models import F
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from .models import Payment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class PaymentListView(ListView):
    template_name = 'payment_list.html'
    model = Payment
    paginate_by = 15
    def get_context_data(self, **kwargs):
        context = super(PaymentListView, self).get_context_data(**kwargs)
        payments = Payment.objects.all().order_by('-id')
        paginator = Paginator(payments, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['payments'] = file_exams
        return context


class PaymentCreateView(CreateView):
    template_name = 'payment_create.html'
    model = Payment
    fields = ['delivery', 'amount', 'counter_party', 'payment_type', 'pay_type']
    success_url = '/payment_list/'

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super(PaymentCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        payment_type = self.request.POST.get('payment_type')
        pay_type = self.request.POST.get('pay_type')
        form.instance.user= self.request.user
        if payment_type == 'D' and pay_type == 'Income':
            CounterParty.objects.filter(pk=self.request.POST.get('counter_party')).update(balance_usd=F('balance_usd') + self.request.POST.get('amount'))
        
        if payment_type == 'S' and pay_type == 'Income':
            CounterParty.objects.filter(pk=self.request.POST.get('counter_party')).update(balance_uzs=F('balance_uzs') + self.request.POST.get('amount'))
            
        if payment_type == 'D' and pay_type == 'Outcome':
            CounterParty.objects.filter(pk=self.request.POST.get('counter_party')).update(balance_usd=F('balance_usd') - self.request.POST.get('amount'))
        
        if payment_type == 'S' and pay_type == 'Outcome':
            CounterParty.objects.filter(pk=self.request.POST.get('counter_party')).update(balance_uzs=F('balance_uzs') - self.request.POST.get('amount'))
        return super(PaymentCreateView, self).form_valid(form)


class PaymentUpdateView(UpdateView):
    template_name = 'payment_udate.html'
    model = Payment
    fields = ['delivery', 'amount', 'counter_party', 'payment_type', 'pay_type']
    success_url = '/payment_list/'