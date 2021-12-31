from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from timogen import views

urlpatterns = [
    path('pdf', views.some_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
