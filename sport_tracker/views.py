from django.shortcuts import render

from .models import Sport

def index(request):
    """The home page for SportExpress."""
    return render(request, 'sport_tracker/index.html')

def sports(request):
    """Show all sports."""
    sports = Sport.objects.order_by('date_added')
    context = {'sports': sports}
    return render(request, 'sport_tracker/sports.html', context)

def sport(request, sport_id):
    """Show a single sport and all its entries."""
    sport = Sport.objects.get(id=sport_id)
    entries = sport.entry_set.order_by('-date_added')
    context = {'sport': sport, 'entries': entries}
    return render(request, 'sport_tracker/sport.html', context)