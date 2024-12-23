from django.shortcuts import render, redirect

from .models import Sport
from .forms import SportForm

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

def new_sport(request):
    """Add a new sport."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = SportForm()
    else:
        # POST data submitted; process data.
        form = SportForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('sport_tracker:topics')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'sport_tracker/new_sport.html', context)