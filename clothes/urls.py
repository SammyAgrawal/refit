from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="clothes_home"),
    path('<int:cloth_id>/', views.item, name = "item")
]

