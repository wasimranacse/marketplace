from django.urls import path
from . import views
app_name = 'item'

urlpatterns = [
    path('add-item/', views.addNewItem, name='add-item'),
    path('<int:pk>/', views.detailView, name='detail'),
]