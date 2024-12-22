from django.shortcuts import render

def index(request):
    """The home page for SportExpress."""
    return render(request, 'sport_tracker/index.html')