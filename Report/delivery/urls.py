from django.urls import path
from .views import  DeliveryListView ,DeliverCreateView, DeliverUpdateView

urlpatterns = [
    path('delivery/', DeliveryListView.as_view(), name='delivery'),
    path('deliver-created/', DeliverCreateView.as_view(), name='deliver-created'),
    path('deliver-update/<int:pk>', DeliverUpdateView.as_view(), name='deliver_update'),
  
   
]
    # path('outlay/update/<int:pk>', OutlayUpdateView.as_view(), name='outlay-payment-update'),
