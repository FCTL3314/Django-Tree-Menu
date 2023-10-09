from django.views.generic.detail import DetailView

from menus.models import Menu


class MenuDetailView(DetailView):
    queryset = Menu.objects.select_related("parent")
    template_name = "index.html"
