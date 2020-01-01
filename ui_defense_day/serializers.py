from rest_framework import serializers
from . import models
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueForYearValidator




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username"]

class PresenterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = models.Presenter
        fields = ["name","username","supervisor", "password", "phone_number"]

    def create(self, validated_data):

        presenter= models.Presenter.objects.create_presenter(username=validated_data["username"] , password=validated_data["password"],job="presenter" , phone_number=validated_data["phone_number"] , supervisor=validated_data["supervisor"], name=validated_data["name"])
        presenter.supervisor=validated_data["supervisor"]
        return presenter


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model=models.Student
        fields = ["name","username","password","phone_number"]

    def create(self, validated_data):
        return  models.Student.objects.create_user(username=validated_data["username"] , password=validated_data["password"],job="student" , phone_number=validated_data["phone_number"],name=validated_data["name"])


class ProfessorSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model=models.Student
        fields = ["name","username","password","phone_number"]

    def create(self, validated_data):
        return  models.Professor.objects.create_user(username=validated_data["username"] , password=validated_data["password"],job="professor" , phone_number=validated_data["phone_number"],name=validated_data["name"])


class IndustrySerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = models.Presenter
        fields = ["name","username", "password", "phone_number"]

    def create(self, validated_data):
        return models.Industry.objects.create_user(username=validated_data["username"] , password=validated_data["password"],job="industry" , phone_number=validated_data["phone_number"],name=validated_data["name"] )


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


class DocumentSerializer(serializers.ModelSerializer):
    presenter = serializers.CharField(
        read_only=True
    )
    class Meta:
        model = models.Document
        fields = "__all__"

    # def create(self, validated_data):
    #     print("validated_data",validated_data)
    #     document=models.Document(presenter=validated_data["presenter"] , file1=validated_data["file1"],file2=validated_data["file2"])
    #     document.save()
    #     return document

class DocumentSerializer2(DocumentSerializer):
    class Meta:
        model = models.Document
        fields = "__all__"

    def create(self, validated_data):
        print("validated_data", validated_data)
        presenter=models.Presenter.objects.get(id=validated_data["presenter"])
        document = models.Document(presenter=presenter, file1=validated_data["file1"],
                                   file2=validated_data["file2"])
        document.save()
        return document

