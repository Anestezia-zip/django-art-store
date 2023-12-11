from django.contrib import admin

from .models import PaintingRequest


@admin.register(PaintingRequest)
class PaintingRequestAdmin(admin.ModelAdmin):
    list_display = ('description', 'size', 'add_signature', 'examples')

