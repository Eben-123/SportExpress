from django.shortcuts import render

from .models import Sport

def index(request):
    """The home page for SportExpress."""
    return render(request, 'sport_tracker/index.html')

def sports(request):
    """Show all sports."""
    topics = Sport.objects.order_by('date_added')
    context = {'sports': sports}
    return render(request, 'sport_tracker/sports.html', context)