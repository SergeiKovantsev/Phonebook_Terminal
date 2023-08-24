from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_entry, name='add_entry'),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('detail/<int:entry_id>/', views.detail_entry, name='detail_entry'),
]