from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=255)
    jersey_number = models.IntegerField(unique=True, blank=True, null=True)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    years_left_on_contract = models.PositiveIntegerField()

    def __str__(self):
        return self.name
