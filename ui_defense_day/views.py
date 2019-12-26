import rest_registration.api.views as register_view
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import generics
from . import models,serializers



@staff_member_required
def Register(request):
    register = register_view.register(request)
    print(register.data)
    return register


class CreatePresenter(generics.CreateAPIView):
    queryset = models.Presenter.objects.all()
    serializer_class = serializers.PresnterSerializer



