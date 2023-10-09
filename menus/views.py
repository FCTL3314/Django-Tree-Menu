from django.views.generic.detail import DetailView

from menus.models import Menu


class MenuDetailView(DetailView):
    queryset = Menu.objects.all()
    template_name = "index.html"
