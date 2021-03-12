from django.views.generic import CreateView, ListView, UpdateView
from .models import CounterParty
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


    
class CounterPartyListView(ListView):
    template_name = 'con_party_list.html'
    model = CounterParty
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super(CounterPartyListView, self).get_context_data(**kwargs)
        conpartylist = CounterParty.objects.all().order_by('-id')
        paginator = Paginator(conpartylist, self.paginate_by)
      
        page = self.request.GET.get('page')
       
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
       
        context['conpartylist'] = file_exams
        
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