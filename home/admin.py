from django.contrib import admin

from .models import PaintingRequest, TemporaryPaintingRequest


@admin.register(PaintingRequest)
class PaintingRequestAdmin(admin.ModelAdmin):
    list_display = ('description', 'size', 'add_signature', 'examples', 'examples2')


@admin.register(TemporaryPaintingRequest)
class PaintingRequestAdmin(admin.ModelAdmin):
    list_display = ('description', 'size', 'add_signature', 'examples', 'examples2')