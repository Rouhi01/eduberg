from django.urls import path
from . import views

app_name = 'api-v1'
urlpatterns = [
    path('Signup', views.SignupApiView.as_view(), name='Signup')
]