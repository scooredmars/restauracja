from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Restaurant(models.Model):
    def __str__(self):
        return self
