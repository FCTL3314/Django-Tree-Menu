from django.urls import path

from menus.views import MenuDetailView

app_name = "menus"

urlpatterns = [
    path("<slug:slug>/", MenuDetailView.as_view(), name="menu-detail"),
]
