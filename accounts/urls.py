from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup', UserSignupView.as_view(), name='login'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='login'),
    path('list', UserListView.as_view(), name='login'),
]