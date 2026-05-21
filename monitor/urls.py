from django.urls import path

from .views import dashboard, system_stats


urlpatterns = [

    path('', dashboard),

    path('stats/', system_stats),

]