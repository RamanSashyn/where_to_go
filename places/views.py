from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    serialized_places = []

    for place in Place.objects.all():
        serialized_places.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude],
                },
                "properties": {
                    "title": place.title,
                    "placeId": str(place.id),
                    "detailsUrl": reverse("place-details", args=[place.id]),
                },
            }
        )

    geojson = {"type": "FeatureCollection", "features": serialized_places}

    context = {
        "places_geojson": geojson,
    }

    return render(request, "index.html", context)


def place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
    )

    serialized_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        },
    }

    return JsonResponse(
        serialized_place,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
