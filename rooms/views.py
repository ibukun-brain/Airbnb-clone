from django.views import generic

from rooms.models import Room


class RoomListView(generic.ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'
    paginate_by = 20
    ordering = '-created_at'
    paginate_orphans = 5


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'
