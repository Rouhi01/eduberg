from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/v1/', include('accounts.api.v1.urls'))
]