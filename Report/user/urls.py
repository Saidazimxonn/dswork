
from django.urls import path
from user.views import  WorkersView, WorkerCreateView, WorkerUpdateView



urlpatterns = [
    path('workers/', WorkersView.as_view(), name='worker'),
    path('worker/create/', WorkerCreateView.as_view(), name='worker_create'),
    path('worker/update/<int:pk>/', WorkerUpdateView.as_view(), name='worker_update'),
]
