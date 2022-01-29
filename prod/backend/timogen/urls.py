from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path("", NomenclatureList.as_view()),
    path("<int:pk>", NomenclatureDetail.as_view()),
    path("location", LocationList.as_view()),
    path("location/<int:pk>", LocationDetail.as_view()),
    path("patho", PathoList.as_view()),
    path("patho/<int:pk>", PathoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
