import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = "Load place from JSON URL"

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="URL to JSON file")

    def handle(self, *args, **options):
        json_url = options["json_url"]
        response = requests.get(json_url)
        response.raise_for_status()

        place_payload = response.json()
        title = place_payload["title"]
        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                "short_description": place_payload.get("description_short", ""),
                "long_description": place_payload.get("description_long", ""),
                "latitude": place_payload["coordinates"]["lat"],
                "longitude": place_payload["coordinates"]["lng"],
            },
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Place "{title}" already exists.'))
            return

        for idx, image_url in enumerate(place_payload["imgs"]):
            img_response = requests.get(image_url)
            img_response.raise_for_status()

            image_name = os.path.basename(image_url)
            image = Image(place=place, position=idx)
            image.image.save(image_name, ContentFile(img_response.content), save=True)

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded "{title}"'))
