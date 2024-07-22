from django.urls import path
from bookapp.api.views import (api_create_book_view, 
                               api_detail_book_view,
                               api_update_book_view,
                               room_list_view,
                               apiOverView)

urlpatterns = [
    path('create', api_create_book_view, name='api_create_book'),
    path('<int:bookid>/', api_detail_book_view, name="detail"),
	path('<str:bookid>/update', api_update_book_view, name="update"),
    path('overview/', apiOverView, name='api_overview'),

    path('rooms/', room_list_view, name='room-list'),
]