from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from therapist import views

urlpatterns = [
    path('', views.TherapistList.as_view()),
    path('<int:pk>/', views.TherapistDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
