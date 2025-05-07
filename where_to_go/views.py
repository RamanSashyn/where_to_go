import json
from django.shortcuts import render
from places.models import Place

def index(request):
    places = []

    for place in Place.objects.all():
        places.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": str(place.id),
                "detailsUrl": "#"
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": places
    }

    context = {
        'places_geojson': geojson,
    }

    return render(request, 'index.html', context)
