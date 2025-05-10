import requests
import os
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load place from JSON URL'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='URL to JSON file')

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()

        data = response.json()
        title = data['title']
        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'short_description': data.get('description_short', ''),
                'long_description': data.get('description_long', ''),
                'latitude': data['coordinates']['lat'],
                'longitude': data['coordinates']['lng'],
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Place "{title}" already exists.'))
            return

        for idx, image_url in enumerate(data['imgs']):
            img_response = requests.get(image_url)
            img_response.raise_for_status()

            image_name = os.path.basename(image_url)  # Брать имя файла из URL
            image = Image(place=place, position=idx)
            image.image.save(
                image_name,
                ContentFile(img_response.content),
                save=True
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded "{title}"'))
