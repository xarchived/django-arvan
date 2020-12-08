from django.urls import path

from arvan import views

urlpatterns = [
    path('generate_request/', views.generate_request)
]
