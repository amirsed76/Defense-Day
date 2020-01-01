from rest_framework import routers
from . import views
from django.urls import path, include,re_path

router = routers.DefaultRouter()

router.register(r'register/students', views.Students_account)
router.register(r'register/professor', views.Professor_account)
router.register(r'register/presenter', views.Presenter_account)
router.register(r'register/industry', views.Industry_account)
router.register(r'my_documents', views.MyDocument)

urlpatterns = [
    path('', include(router.urls)),

    path("documents/",views.Documentviewset.as_view()),
]