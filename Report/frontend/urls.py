from django.urls import path
from .views import BaseView, LoginView


urlpatterns = [

        path('', BaseView.as_view(), name='base'),
        path('login/', LoginView.as_view(), name='login-view'),
]
