from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Sport, Entry
from .forms import SportForm, EntryForm

def index(request):
    """The home page for SportExpress."""
    return render(request, 'sport_tracker/index.html')

@login_required
def sports(request):
    """Show all sports."""
    sports = Sport.objects.filter(owner=request.user).order_by('date_added')
    context = {'sports': sports}
    return render(request, 'sport_tracker/sports.html', context)

@login_required
def sport(request, sport_id):
    """Show a single sport and all its entries."""
    sport = Sport.objects.get(id=sport_id)
    # Make sure the sport belongs to the current user.
    if sport.owner != request.user:
        raise Http404
    
    entries = sport.entry_set.order_by('-date_added')
    context = {'sport': sport, 'entries': entries}
    return render(request, 'sport_tracker/sport.html', context)

@login_required
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

@login_required
def new_entry(request, sport_id):
    """Add a new entry for a particular sport."""
    sport = Sport.objects.get(id=sport_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.sport = sport
            new_entry.save()
            return redirect('sport_tracker:sport', sport_id=sport_id)
    
    # Display a blank or invalid form.
    context = {'sport': sport, 'form': form}
    return render(request, 'sport_tracker/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit and existing entry."""
    entry = Entry.objects.get(id=entry_id)
    sport = entry.sport
    if sport.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('sport_tracker:sport', sport_id=sport.id)
    
    context = {'entry': entry, 'sport': sport, 'form': form}
    return render(request, 'sport_tracker/edit_entry.html', context)