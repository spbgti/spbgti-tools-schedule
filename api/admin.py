from django.contrib import admin

from .models import Exercise
from .models import Schedule

admin.site.register(Schedule)
admin.site.register(Exercise)
