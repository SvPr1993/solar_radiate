from django.db import models


class Data(models.Model):
    date = models.DateField(unique=True)
    activity = models.CharField(max_length=100, default='default_value')
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date}: {self.activity}"
