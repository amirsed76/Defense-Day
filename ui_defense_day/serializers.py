from . import models
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueForYearValidator
from rest_framework import serializers

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
        fields = ["id","name", "username", "supervisor", "password", "phone_number"]

    def create(self, validated_data):
        presenter = models.Presenter.objects.create_presenter(username=validated_data["username"],
                                                              password=validated_data["password"], job="presenter",
                                                              phone_number=validated_data["phone_number"],
                                                              supervisor=validated_data["supervisor"],
                                                              name=validated_data["name"])
        presenter.supervisor = validated_data["supervisor"]
        return presenter

    def update(self, instance, validated_data):
        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        info = serializers.model_meta.get_field_info(instance)


        for attr, value in validated_data.items():
            print(attr)
            if attr == "password":
                print("ok")
                field = getattr(instance, attr)
                instance.set_password(value)
            elif attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance

class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = models.Student
        fields = ["id","name", "username", "password", "phone_number"]

    def create(self, validated_data):
        return models.Student.objects.create_user(username=validated_data["username"],
                                                  password=validated_data["password"], job="student",
                                                  phone_number=validated_data["phone_number"],
                                                  name=validated_data["name"])

    def update(self, instance, validated_data):
        print("UPDATE")
        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        info = serializers.model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            print(attr)
            if attr == "password":
                print("ok")
                field = getattr(instance, attr)
                instance.set_password(value)
            elif attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance


class ProfessorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = models.Student
        fields = ["id","name", "username", "password", "phone_number"]

    def create(self, validated_data):
        print("create professor")
        return models.Professor.objects.create_user(username=validated_data["username"],
                                                    password=validated_data["password"], job="Professor",
                                                    phone_number=validated_data["phone_number"],
                                                    name=validated_data["name"])
    def update(self, instance, validated_data):
        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        info = serializers.model_meta.get_field_info(instance)


        for attr, value in validated_data.items():
            print(attr)
            if attr == "password":
                print("ok")
                field = getattr(instance, attr)
                instance.set_password(value)
            elif attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance


class IndustrySerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = models.Industry
        fields = ["name", "username", "password", "phone_number"]

    def create(self, validated_data):
        return models.Industry.objects.create_user(username=validated_data["username"],
                                                   password=validated_data["password"], job="industry",
                                                   phone_number=validated_data["phone_number"],
                                                   name=validated_data["name"])

    def update(self, instance, validated_data):
        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        info = serializers.model_meta.get_field_info(instance)


        for attr, value in validated_data.items():
            print(attr)
            if attr == "password":
                print("ok")
                field = getattr(instance, attr)
                instance.set_password(value)
            elif attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username')
        read_only_fields = ('username',)


class UserRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(write_only=True)
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
        read_only=True,
    )

    class Meta:
        model = models.Document
        fields = "__all__"


class DocumentSerializer2(DocumentSerializer):
    supervisor = serializers.CharField(read_only=True, source='presenter.supervisor')
    class Meta:
        model = models.Document
        fields = ["id","file1","file2","presenter","supervisor"]
