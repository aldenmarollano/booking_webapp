from django.urls import path
from bookapp.views import user_home_screenview

app_name = 'bookapp'
urlpatterns = [
    path('', user_home_screenview, name='home'),
]