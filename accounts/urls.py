from django.urls import path
from accounts.views import UserSigninView

app_name = 'accounts'

urlpatterns = [
    path('login', UserSigninView.as_view(), name='login')
]