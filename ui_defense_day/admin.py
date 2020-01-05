from django import forms

from . import models
from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from jalali_date import datetime2jalali, date2jalali

class EventForm(forms.ModelForm):

    class Meta:
        class Meta:
            model = models.Event
            widgets = {
                'delivery_date': forms.DateInput(attrs={'id': 'datepicker'}),
            }


admin.site.register(models.User)
admin.site.register(models.Presenter)
admin.site.register(models.RoleCoefficent)
admin.site.register(models.Professor)
admin.site.register(models.Student)
admin.site.register(models.Document)
admin.site.register(models.Score)
# admin.site.register(models.Event)
class EventAdmin(admin.ModelAdmin,ModelAdminJalaliMixin):
    from django.contrib import admin
    from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

    @admin.register(models.Event)
    class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
        list_display = ['start_date',"end_date"]
        # list_display = ['start_date',"end_date", 'get_created_jalali']

        formfield_overrides = {}

        # def get_created_jalali(self, obj):
        #     print("type obj",type(obj))
        #     print("obj_start date",obj.start_date)
        #     print("obj_end date",obj.end_date)
        #     # return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
        #     return datetime2jalali(obj.save()).strftime('%y/%m/%d _ %H:%M:%S')



