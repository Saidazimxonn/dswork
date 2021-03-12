from django.contrib.auth.models import Group
from django.views.generic import TemplateView, CreateView, UpdateView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.models import User
from rest_framework import viewsets, status
from user.serializer import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            # sale = Sale.objects.create(dealer_id=dealer_id, invoice=invoice)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as ex:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            # .... Your code ....
            serializer.save()
            return Response(serializer.data)

        except Exception as ex:
            print(ex)

    @action(detail=True, methods=['get'])
    def get_by_username(self, request, pk=None):
        try:
            user = User.objects.get(username=pk)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'Не найдено.'})

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        try:
            instance = self.get_object()
            print(instance)
            print(request.POST)
            if instance.check_password(request.POST['old_password']):
                instance.set_password(request.POST['new_password'])
                instance.save()
                return Response({'ok': True})
            else:
                return Response({'ok': False})
        except Exception as ex:
            print(ex)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class WorkersView(TemplateView):
    template_name = 'worker.html'

    def get_context_data(self, **kwargs):
        context = super(WorkersView, self).get_context_data(**kwargs)
        context['workers'] = User.objects.select_related('order', 'firm').all()
        return context


class WorkerCreateView(CreateView):
    template_name = 'worker_create.html'
    model = User
    fields = ['first_name', 'firm', 'order', 'status', 'salary_type', 'birthday', 'stack', ]
    success_url = '/workers/'


class WorkerUpdateView(UpdateView):
    template_name = 'worker_update.html'
    model = User
    fields = ['first_name', 'firm', 'order', 'status', 'salary_type', 'birthday', 'stack', ]
    success_url = '/workers/'
