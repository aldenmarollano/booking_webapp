from django.urls import path
from bookapp.views import (BldgRegistrationView,
                           RoomBldgListView,
                           RoomRegistrationView,
                           BookedRoomView,
                           CheckedOutView,
                           RoomView
                            )

app_name = 'bookapp'
urlpatterns = [
    path('building/register', BldgRegistrationView.as_view(), name='bldg_register'),
    path('building/room/register', RoomRegistrationView.as_view(), name='add_room'),
    path('', RoomBldgListView.as_view(), name='room_bldg_list'),
    path('booked/', BookedRoomView.as_view(), name='booked'),
    path('booked/<int:id>/', CheckedOutView.as_view(), name='checkout'),
    path('book-a-room/', RoomView.as_view(), name='book_a_room'),
    path('room/<int:id>/', RoomView.as_view(), name='room_data'),
]
