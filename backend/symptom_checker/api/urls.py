from django.urls import path
from .views import SymptomAnalyzer

urlpatterns = [
    path('analyze/', SymptomAnalyzer.as_view(), name='analyze'),
]
