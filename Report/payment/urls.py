from django.urls import path
from .views import PaymentListView ,PaymentCreateView, PaymentUpdateView

urlpatterns = [
    path('payment_list/', PaymentListView.as_view(), name='payment_list'),
    path('payment_create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payment_upadte/<int:pk>', PaymentUpdateView.as_view(), name='payment_update'),
]