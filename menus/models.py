from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Menu(models.Model):
    name = models.CharField(max_length=64, unique=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        if self.slug is None:
            self.slug = slugify(self.name)

    def get_absolute_url(self):
        return reverse("menus:menu-detail", kwargs={"slug": self.slug})
