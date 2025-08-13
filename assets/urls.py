from django.urls import path
from . import views

urlpatterns = [
    path('asset_info/<int:id>/', views.asset_info),
    path('get_ai_summary/<int:id>/', views.get_ai_summary)
]