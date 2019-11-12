from django.urls import path
from .views import DashboardView

app_name    = 'Dashboard'
urlpatterns = [
    path('', DashboardView, name='dashboard_view')
]