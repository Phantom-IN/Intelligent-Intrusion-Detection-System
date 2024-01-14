from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/receive_alert/', views.ReceiveAlert.as_view(), name='receive_alert'),
    path('alerts/', views.alerts, name = 'alerts'),
    path('analysis/', views.analysis, name = 'analysis')
]