from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Categories(models.Model):
    """ Generowanie listy dla strony glownej """

    thumbnail = models.ImageField(verbose_name=_("Home thumbnail"), upload_to="",)
    image = models.ImageField(verbose_name=_("Menu background"), upload_to="",)
    name = models.CharField(verbose_name=_("Name"), max_length=70)

    def get_absolute_url(self):
        return reverse("restaurant:menu", kwargs={"category_pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Menu(models.Model):
    """ Generowanie listy dla menu """

    category = models.ForeignKey(
        Categories, verbose_name=_("Category"), on_delete=models.CASCADE
    )

    dish = models.TextField(verbose_name=_("Dish name"), max_length=150)
    description = models.TextField(verbose_name=_("Ingredients"), max_length=500)
    price = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return self.dish

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")


class Gallery(models.Model):
    """ Generowanie listy dla galeri """

    image = models.ImageField(upload_to="gallery")

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _("gallery")
