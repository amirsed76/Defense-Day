import rest_registration.api.views as register_view
from django.contrib.admin.views.decorators import staff_member_required
import json
from . import models
@staff_member_required
def RegisterStudent(request):
    user = register_view.register(request)
    return user

@staff_member_required
def RegisterStudent(request):
    return register_view.register(request)


@staff_member_required
def RegisterIndustry(request):
    return register_view.register(request)


@staff_member_required
def Registersupervisor(request):
    return register_view.register(request)


@staff_member_required
def RegisterReferee(request):
    return register_view.register(request)
