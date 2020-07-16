from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup, name='signup'), # 회원가입
    path('api-token-auth/', obtain_jwt_token),  # 로그인
]