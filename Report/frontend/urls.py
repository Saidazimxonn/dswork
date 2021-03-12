from django.urls import path
from .views import BaseView, LoginView
from filter.views import FilterView


urlpatterns = [
        path('', FilterView.as_view(), name='base'),
        path('login/', LoginView.as_view(), name='login-view'),
]
