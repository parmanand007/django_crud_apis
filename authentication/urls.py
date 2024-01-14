
from django.urls import path
from authentication.views import RegisterView, CustomTokenObtainPairView,APILogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
urlpatterns = [
    
    path('register', RegisterView.as_view(), name='auth_register'),
    path('login', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('logout', APILogoutView.as_view(), name='auth_logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
