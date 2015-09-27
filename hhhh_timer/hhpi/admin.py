from django.contrib import admin

from .models import Rider
from .models import Checkpoint

admin.site.register(Rider)
admin.site.register(Checkpoint)