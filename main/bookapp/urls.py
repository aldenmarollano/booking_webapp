from django.urls import path
from bookapp.views import (BldgRegistrationView,
                           RoomBldgListView,
                           RoomRegistrationView,
                            )

app_name = 'bookapp'
urlpatterns = [
    # path('', user_home_screenview, name='home'),

    path('building/register', BldgRegistrationView.as_view(), name='bldg_register'),
    path('building/room/register', RoomRegistrationView.as_view(), name='add_room'),
    path('', RoomBldgListView.as_view(), name='room_bldg_list'),

]