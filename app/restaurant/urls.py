from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    # Function View
    # path('details/<int:pk>/', views.post_detail, name='details'),
    path("", views.Home.as_view(), name="index"),
    path("menu/<int:category_pk>", views.Details.as_view(), name="menu"),
]
