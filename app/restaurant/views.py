from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.detail import SingleObjectMixin

from .models import Restaurant


class Home(ListView):
    template_name = 'restaurant/home.html'
    model = Restaurant
    context_object_name = 'Restaurant'
