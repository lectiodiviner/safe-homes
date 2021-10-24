# cases/urls.py
from django.urls import path, re_path
from . import views

app_name = 'cases'

urlpatterns = [
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]
