from rest_framework import serializers
from . import models


class PresnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presenter
        fields = ['presenter','supervisor']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        # fields = ['username','password','role' , 'supervisor']

