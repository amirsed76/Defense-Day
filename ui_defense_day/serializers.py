from rest_framework import serializers
from . import models
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueForYearValidator




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username"]

class PresnterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = models.Presenter
        fields = ["username", "password", "phone_number"]

    def create(self, validated_data):
        return  models.Student.objects.create_user(username=validated_data["username"] , password=validated_data["password"] , role="presenter")


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model=models.Student
        fields = ["username","password","phone_number"]

    def create(self, validated_data):
        return  models.Student.objects.create_user(username=validated_data["username"] , password=validated_data["password"],job="student")


class ProfessorSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model=models.Student
        fields = ["username","password","phone_number"]

    def create(self, validated_data):
        return  models.Student.objects.create_user(username=validated_data["username"] , password=validated_data["password"] ,role="professor")



class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username')
        read_only_fields = ('username',)


class UserRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(write_only=True)
    # email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

