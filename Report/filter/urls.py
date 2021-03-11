from django.urls import path
from .views import FilterView

urlpatterns = [

    path('filter-pay/', FilterView.as_view(), name='filter-pay'),
]