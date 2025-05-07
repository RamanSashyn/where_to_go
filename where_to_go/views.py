from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from places.models import Place
from django.urls import reverse

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
                "detailsUrl": reverse('place-details', args=[place.id]),
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


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_data = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }

    return JsonResponse(
        place_data,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
