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
                                                    password=validated_data["password"], job="professor",
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

class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True,
    )
    supervisor = serializers.CharField(read_only=True, source='presenter.supervisor')
    presenter_username = serializers.CharField(read_only=True, source='presenter.username')

    score=serializers.DecimalField(max_digits=4, decimal_places=2 , max_value=20 , min_value=0)

    class Meta:
        model = models.Score
        fields = ["id","presenter","user","supervisor","presenter_username" , "score"]


class Average(serializers.ModelSerializer):
    average_score = serializers.SerializerMethodField()
    supervisor = serializers.CharField(read_only=True, source='presenter.supervisor')
    presenter_username = serializers.CharField(read_only=True, source='presenter.username')
    class Meta:
        fields = ["id","presenter","average_score","supervisor","presenter_username"]
        model = models.Score
    def get_average_score(self, obj):
        presenter_scores=models.Score.objects.filter(presenter_id=obj.presenter.id )
        scores=[]
        sum_coefficent=0
        for p_score in presenter_scores:
            if p_score.user.job in ["admin","student","industry"]:
                job = p_score.user.job
            elif p_score.user.job=="presenter":
                job = "student"
            elif p_score.user.id == obj.presenter.supervisor.id:
                job = "supervisor"
            else :
                job = "professor"
            try:

                coefficent=models.RoleCoefficent.objects.get(job=job).coefficent
                scores.append(p_score.score * coefficent )
                sum_coefficent += coefficent
                print("__________")
                print("p_score_user", p_score.user)
                print("p_score presenter", p_score.presenter)
                print("coefficent",coefficent)
                print("score",p_score.score)
            except:
                return None
        return sum(scores)/sum_coefficent


