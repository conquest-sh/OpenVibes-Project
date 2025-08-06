from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('overall/', views.overall, name = 'overall'),
    path('overall/<int:overal_id>/', views.overal, name='overal'),
    path('new_overall/', views.new_overall, name='new_overall'),
    path('new_explain/<int:overal_id>/', views.new_explain, name='new_explain'),
    path('edit_overall/<int:overall_id>/', views.edit_overall, name='edit_overall'),
]