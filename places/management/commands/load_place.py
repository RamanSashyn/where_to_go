import os
import sys
import time

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from requests.exceptions import ConnectionError, HTTPError

from places.models import Image, Place


class Command(BaseCommand):
    help = "Load place from JSON URL"

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="URL to JSON file")

    def handle(self, *args, **options):
        json_url = options["json_url"]
        try:
            response = requests.get(json_url)
            response.raise_for_status()
        except (HTTPError, ConnectionError) as e:
            self.stderr.write(f"Ошибка при загрузке JSON: {e}")
            return

        raw_place = response.json()
        title = raw_place["title"]
        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                "short_description": raw_place.get("description_short", ""),
                "long_description": raw_place.get("description_long", ""),
                "latitude": raw_place["coordinates"]["lat"],
                "longitude": raw_place["coordinates"]["lng"],
            },
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Place "{title}" already exists.'))
            return

        for idx, image_url in enumerate(raw_place["imgs"]):
            try:
                img_response = requests.get(image_url)
                img_response.raise_for_status()
            except HTTPError as e:
                print(f"❌ Ошибка HTTP при загрузке изображения {image_url}: {e}", file=sys.stderr)
                continue
            except ConnectionError as e:
                print(f"🔌 Потеря соединения при загрузке изображения {image_url}: {e}", file=sys.stderr)
                time.sleep(5)
                continue

            image_name = os.path.basename(image_url)
            Image.objects.create(
                place=place,
                position=idx,
                image=ContentFile(img_response.content, name=image_name)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded "{title}"'))
