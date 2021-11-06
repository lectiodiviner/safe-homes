from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Case
from django import forms
from ckeditor.widgets import CKEditorWidget

class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Case
        fields = '__all__'



@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'title', 'thumbnail_image',  'is_view', 'created_at', 'tag_list']
    list_editable = ['is_view']
    list_filter = ['is_view', 'created_at']
    search_fields = ['id', 'created_by', 'title']
    form = EventAdminForm
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
