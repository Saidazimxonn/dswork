from django.urls import path
from .views import  CounterPartyListView, CounterPartyCreateView, CounterPartyUpdate


urlpatterns = [
    path('con-party/', CounterPartyListView.as_view(), name='con_party'),
    path('con-party-creat/', CounterPartyCreateView.as_view(), name='con_party_creat' ),
    path('con-party-update/update/<int:pk>/', CounterPartyUpdate.as_view(), name='con_party_update'),
   
]
    
