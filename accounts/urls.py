from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserView, UserDetail, UserCreateAPI, UserListAPI


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/accounts_login.html'), name='login'),  # 로그인 URL
    path('logout/', LogoutView.as_view(template_name='accounts/accounts_logout.html'), name='logout'),  # 로그아웃 URL
    path('', UserView.as_view()),  # 기본 rest_framework URL
    path('detail/<int:pk>/', UserDetail.as_view()),  # 기본 rest_framework 디테일 URL
    path('create/', UserCreateAPI.as_view(), name='user_create'),  # views 에 유저 생성 URL
    path('list/', UserListAPI.as_view(), name='user_list'),  # views 에 유저 list URL
]
