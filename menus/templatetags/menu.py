from django import template
from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string

from menus.models import Menu

register = template.Library()


class DrawMenuMetadata:
    is_target_menu_reached: bool = False
    is_first: bool = True


@register.simple_tag
def draw_menu(
    menu: Menu,
    request: WSGIRequest,
    metadata: DrawMenuMetadata | None = None,
) -> str:
    """
    Draws the menu and all its children.
    """
    if metadata is None:
        metadata = DrawMenuMetadata()
    if metadata.is_first:
        menu = menu.get_first_parent()
        metadata.is_first = False
    if is_active := request.path == menu.get_absolute_url():
        metadata.is_target_menu_reached = True
    context = {
        "menu": menu,
        "children": menu.children.all(),
        "is_active": is_active,
        "metadata": metadata,
        "request": request,
    }
    return render_to_string("menu.html", context)
