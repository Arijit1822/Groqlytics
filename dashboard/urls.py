from django.urls import path
from . import views

urlpatterns = [
    path('reset_history/', views.reset_history, name='reset_history'),
    path('save_logs_pdf/', views.save_logs_pdf, name='save_logs_pdf'),
    path('api/system/', views.system_api, name='system_api'),
]