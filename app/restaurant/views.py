from django.views.generic import DetailView, ListView

from .models import Categories, Gallery, Menu


class Home(ListView):
    template_name = "restaurant/home.html"
    model = Categories
    context_object_name = "categories"


class Details(ListView):
    template_name = "restaurant/menu-details.html"
    model = Menu
    context_object_name = "entries"
    pk_url_kwarg = "category_pk"

    def get_queryset(self):
        return Menu.objects.filter(category=self.kwargs[self.pk_url_kwarg])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Categories.objects.all()
        context["active_category"] = Categories.objects.get(
            pk=self.kwargs[self.pk_url_kwarg]
        )
        return context


class Photos(ListView):
    template_name = "restaurant/gallery.html"
    model = Gallery
    context_object_name = "gallery"
