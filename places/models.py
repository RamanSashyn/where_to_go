from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = models.TextField('Полное описание', blank=True)
    latitude = models.FloatField('Широта', blank=True, null=True)
    longitude = models.FloatField('Долгота', blank=True, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField('Картинка', upload_to='places')
    position = models.PositiveIntegerField('Позиция', default=0, blank=False, null=False)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.place.title} - {self.position}"