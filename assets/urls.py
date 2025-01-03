from django.urls import path
from . import views

urlpatterns = [
    path('asset_info/<int:id>/', views.asset_info)
]