from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('legend/<int:legend_id>/', views.legend_detail, name='legend_detail'),
]
