from django.urls import path
from .views import (
    RegisterView, LoginView,UserListCreateView, UserDetailView,
    SensorListCreateView, SensorDetailView, DataListCreateView,
    DataDetailView, AlertListCreateView, AlertDetailView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensors/<int:sensor_id>/data/', DataListCreateView.as_view(), name='data-list'),
    path('sensors/<int:sensor_id>/data/<int:pk>/', DataDetailView.as_view(), name='data-detail'),
    path('sensors/<int:sensor_id>/alerts/', AlertListCreateView.as_view(), name='alert-list'),
    path('sensors/<int:sensor_id>/alerts/<int:pk>/', AlertDetailView.as_view(), name='alert-detail'),
]
