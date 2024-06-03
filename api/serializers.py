from rest_framework import serializers
from .models import User, Sensor, Data, Alert


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        extra_kwargs = {'sensor': {'read_only': True}}


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        extra_kwargs = {'sensor': {'read_only': True}}

