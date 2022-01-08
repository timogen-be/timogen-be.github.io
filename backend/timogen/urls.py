from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', NomenclatureList.as_view()),
    path('<int:pk>', NomenclatureDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
