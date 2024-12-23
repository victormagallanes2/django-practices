


#from braces.views import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model


class UserListView(generic.ListView):
    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'chat/chat.html'
