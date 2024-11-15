from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.list_uploaded_files, name='list_uploaded_files'),
]