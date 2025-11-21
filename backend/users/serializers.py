from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role', read_only=True)
    student_id = serializers.CharField(source='username', read_only=True)

    class Meta:
        model = User
        fields = ('student_id', 'email', 'role')


class RegisterSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=[('student','Student'),('teacher','Teacher'),('admin','Admin')])
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_student_id(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('student_id already exists')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('email already exists')
        return value

    def create(self, validated_data):
        student_id = validated_data['student_id']
        email = validated_data['email']
        role = validated_data['role']
        password = validated_data['password']

        user = User.objects.create_user(username=student_id, email=email, password=password)
        user.profile.role = role
        user.profile.save()
        return user


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # student_id or email
    password = serializers.CharField(write_only=True)
