from django.contrib import admin

# Register your models here.
from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'title', 'thumbnail_image',  'is_view', 'created_at', 'tag_list']
    list_editable = ['is_view']
    list_filter = ['is_view', 'created_at']
    search_fields = ['id', 'created_by', 'title']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())