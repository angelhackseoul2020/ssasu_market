from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup, name='signup'), # 회원가입
    path('api-token-auth/', obtain_jwt_token),  # 로그인
    path('myinfo/<str:userid>/', views.myinfo, name='myinfo'),  # id로 정보 주기
    path('editinfo/<int:user_id>/', views.editinfo, name='editinfo'),
    path('get_users/', views.get_users, name='get_users'),
]