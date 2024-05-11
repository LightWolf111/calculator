from django.db import models

class Room(models.Model):
    length = models.FloatField(verbose_name='Длина помещения (в метрах)')
    width = models.FloatField(verbose_name='Ширина помещения (в метрах)')

    def calculate_area(self):
        return self.length * self.width

    def __str__(self):
        return f'Помещение: {self.id}'
