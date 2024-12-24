"""Defines URL patterns for sport_tracker."""

from django.urls import path

from . import views

app_name = 'sport_tracker'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all sports.
    path('sports/', views.sports, name='sports'),
    # Detail page for a single topic.
    path('sports/<int:sport_id>/', views.sport, name='sport'),
    # Page for adding a new sport
    path('new_sport/', views.new_sport, name='new_sport'),
]