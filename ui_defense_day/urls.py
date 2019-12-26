from django.urls import path , include
from . import views
urlpatterns = [

    path('register/', views.Register),
    path('register/presenter', views.CreatePresenter.as_view()),

]