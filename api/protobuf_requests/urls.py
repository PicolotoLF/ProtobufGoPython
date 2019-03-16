from django.urls import path
from .views import ResponseView


urlpatterns = [
    path('responses/', ResponseView.as_view(), name="responses-all")
]