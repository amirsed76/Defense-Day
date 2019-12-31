import rest_registration.api.views as register_view
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import generics,viewsets,mixins
from . import models,serializers
from rest_auth.registration.views import RegisterView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework import status




@staff_member_required
def Register(request):
    if request.method == "GET":
        register = register_view.register(request)
        print(register.data)
        return register


class CreatePresenter(generics.CreateAPIView , generics.UpdateAPIView , generics.DestroyAPIView):
    queryset = models.Presenter.objects.all()
    serializer_class = serializers.PresnterSerializer



class Students_account(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    # permission_classes = [IsAdminUser]



class Professor_account(viewsets.ModelViewSet):
    serializer_class = serializers.ProfessorSerializer
    queryset = models.Professor.objects.all()
    permission_classes = [IsAdminUser]




class SalesmanList(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


