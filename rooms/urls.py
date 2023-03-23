from django.urls import path

from rooms import views as room_views

app_name = 'rooms'

urlpatterns = [
    path(
        '',
        room_views.RoomListView.as_view(),
        name='room-list',
    ),
    path(
        '<int:pk>/',
        room_views.RoomDetailView.as_view(),
        name='room-detail',
    )
]
