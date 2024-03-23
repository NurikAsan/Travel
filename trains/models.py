from django.db import models
from django.forms import ValidationError
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=20, unique=True)
    travel_time = models.PositiveSmallIntegerField()
    from_city = models.ForeignKey(City, models.CASCADE, 'from_city_set')
    to_city = models.ForeignKey(City, models.CASCADE, 'to_city_set')


    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = 'travel_time',

    def __str__(self) -> str:
        return self.name


    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Похожие города')
        qt = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(pk=self.pk)
        if qt.exists():
            raise ValidationError('Изменить время в пути')
