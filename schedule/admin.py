from django.contrib import admin

from .models import Schedule
from .models import ClassRecord

admin.site.register(Schedule)
admin.site.register(ClassRecord)