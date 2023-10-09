from django import template
from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string

from menus.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu: Menu, request: WSGIRequest) -> str:
    context = {
        "menu": menu,
        "children": menu.children.all(),
        "active_class": "active" if request.path == menu.get_absolute_url() else "",
        "request": request,
    }
    return render_to_string("menu.html", context)
