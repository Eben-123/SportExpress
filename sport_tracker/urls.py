"""Defines URL patterns for sport_tracker."""

from django.urls import path

from . import views

app_name = 'sport_tracker'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all sports.
    path('sports/', views.sports, name='sports'),
]