from django.urls import path
from account.views import user_registration_view, user_home_screenview

app_name = 'account'
urlpatterns = [
    # path('register/', UserRegistrationView.as_view(), name='register_user'),
    path('register/', user_registration_view, name='register_user'),
    path('home/', user_home_screenview, name='home'),
]