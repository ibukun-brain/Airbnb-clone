from django.views import generic

from rooms.models import Room


class IndexView(generic.ListView):
    model = Room
    context_object_name = 'rooms'
    paginate_by = 20
    template_name = 'home/index.html'
