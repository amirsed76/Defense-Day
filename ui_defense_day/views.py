import rest_registration.api.views as register_view
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import generics,viewsets,mixins
from . import models,serializers
from rest_auth.registration.views import RegisterView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework import status
from . import permissions




@staff_member_required
def Register(request):
    if request.method == "GET":
        register = register_view.register(request)
        print(register.data)
        return register


class Industry_account(viewsets.ModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = serializers.IndustrySerializer
    permission_classes = [IsAdminUser]




class Presenter_account(viewsets.ModelViewSet):
    queryset = models.Presenter.objects.all()
    serializer_class = serializers.PresenterSerializer
    permission_classes = [IsAdminUser]




class Students_account(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAdminUser]



class Professor_account(viewsets.ModelViewSet):
    serializer_class = serializers.ProfessorSerializer
    queryset = models.Professor.objects.all()
    permission_classes = [IsAdminUser]




class MyDocument(viewsets.ModelViewSet):
    serializer_class = serializers.DocumentSerializer
    queryset = models.Document.objects.all()
    permission_classes = [permissions.IsPresenter]

    def get_queryset(self):
        return models.Document.objects.filter(presenter=self.request.user)

    def create(self, request, *args, **kwargs):
        data=request.data
        print("data",data)
        serializer = serializers.DocumentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        print("_dataaaaaa",data)
        presenter=models.Presenter.objects.get(id=request.user.id)
        data["presenter"]=presenter
        document=models.Document(presenter=data["presenter"], file1=data["file1"],file2=data["file2"])
        document.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer, status=status.HTTP_201_CREATED, headers=headers)


class DocumentListView(generics.ListAPIView):
    serializer_class = serializers.DocumentSerializer2
    queryset = models.Document.objects.all()
    permission_classes = []


class ProfessorStudentsDocumentListView(generics.ListAPIView):
    serializer_class = serializers.DocumentSerializer2
    queryset = models.Document.objects.all()
    permission_classes = [permissions.Isprofessor]

    def get_queryset(self):
        return models.Document.objects.filter(presenter__supervisor__id=self.request.user.id)
