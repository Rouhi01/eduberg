from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'api-v1'
urlpatterns = [
    path('signup', views.SignupApiView.as_view(), name='signup'),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('logout/', views.LogoutApiView.as_view(), name='logout'),
    path('logout_all/', views.LogoutAllApiView.as_view(), name='logout_all')
]