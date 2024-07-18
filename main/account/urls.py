from django.urls import path
from account.views import ( user_registration_view,
                            login_view, logout_view,
                            account_view )


app_name = 'account'
urlpatterns = [
    path('register/', user_registration_view, name='register_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<username>/', account_view, name='profile')
]