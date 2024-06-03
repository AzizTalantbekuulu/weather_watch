from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User, Sensor, Data, Alert
from .serializers import RegisterSerializer, UserSerializer, DataSerializer, AlertSerializer, SensorSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        response.data['refresh'] = str(refresh)
        response.data['access'] = str(refresh.access_token)
        return response


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=400)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]


class DataListCreateView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sensor_id = self.kwargs.get('sensor_id')
        sensor = Sensor.objects.get(pk=sensor_id)
        serializer.save(sensor=sensor)


class DataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]


class AlertListCreateView(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sensor_id = self.kwargs.get('sensor_id')
        sensor = Sensor.objects.get(pk=sensor_id)
        serializer.save(sensor=sensor)


class AlertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]
