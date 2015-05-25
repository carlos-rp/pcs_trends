from django.contrib import admin

from .models import Tag
from .models import Trend
from .models import TagInTrend

admin.site.register(Tag)
admin.site.register(Trend)
admin.site.register(TagInTrend)
