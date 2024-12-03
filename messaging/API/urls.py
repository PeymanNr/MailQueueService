from django.urls import path
from messaging.API.views import EmailAPIView

urlpatterns = [
    path('send/', EmailAPIView.as_view(), name='send-email')
]