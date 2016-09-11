from django.contrib import admin

from .models import Group
from .models import Location
from .models import Room
from .models import Teacher

admin.site.register(Group)
admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Teacher)