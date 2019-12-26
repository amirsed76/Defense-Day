from django.urls import path , include
from . import views
urlpatterns = [
    path('register/student/', views.RegisterStudent),
    path('register/industry/', views.RegisterIndustry),
    path('register/supervisor/', views.Registersupervisor),
    path('register/Referee/', views.RegisterReferee),

]