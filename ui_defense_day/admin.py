
from . import models

from django.conf.urls import url
from django.contrib import admin
# import  rest_registration.api.views as register_view


admin.site.register(models.User)
admin.site.register(models.Presenter)
admin.site.register(models.RoleCoefficent)
admin.site.register(models.Professor)
admin.site.register(models.Student)
admin.site.register(models.Document)