from rest_framework import serializers
from . import models




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class PresnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presenter
        # fields =["presenter" , "supervisor"]
        fields = '__all__'
