from django.shortcuts import render, get_object_or_404
from .models import Event

# Home view to render the image map
def home(request):
    return render(request, 'events/home.html', {"themes": themes})# Hardcoded themes
themes = {
    1: {"name": "Living Room", "description": "A fascinating look at a 1963 living room."},
    2: {"name": "Artifacts of 1963", "description": "Explore the artifacts of a historical year."},
    3: {"name": "Bedroom", "description": "A 1963 bedroom."},
    4: {"name": "Civil Rights", "description": "Dive into the Civil Rights movement."},
    5: {"name": "Womens Rights", "description": "A tribute to the Women's Rights movement."},
    6: {"name": "Telephone", "description": "Discover the invention of the telephone."},
    7: {"name": "JFK", "description": "John F. Kennedy: A legacy of leadership."},
    8: {"name": "World Expo", "description": "The World Expo and its impact."},
}

from django.shortcuts import render, get_object_or_404
from .models import Event

def theme_events(request, theme_id):
    theme = themes.get(theme_id)
    if not theme:
        return render(request, "404.html")  # 404 page for invalid themes
    
    events = Event.objects.filter(theme_id=theme_id).order_by('date')  # Fetch all events for the theme
    return render(request, "events/theme_events.html", {
        "theme": theme,
        "events": events,
    })

# View to render individual event details
def event_detail(request, theme_id, event_id):
    theme = themes.get(theme_id)
    event = get_object_or_404(Event, id=event_id)

    # Pass theme_id to the context
    return render(request, "events/event_detail.html", {
        "theme": theme,
        "event": event,
        "theme_id": theme_id,
    })
def alternative_page(request):
    return render(request, "events/alternative_page.html")
