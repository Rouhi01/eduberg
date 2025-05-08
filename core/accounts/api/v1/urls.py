from django.urls import path
from . import views

app_name = 'api-v1'
urlpatterns = [
    path('login', views.login_api_view, name='login')
]