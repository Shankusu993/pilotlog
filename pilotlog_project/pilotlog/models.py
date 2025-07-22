from django.db import models

class Aircraft(models.Model):
    make = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    reference = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.reference

class Airfield(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    date = models.DateField()
    departure_airfield = models.ForeignKey(Airfield, related_name='departures', on_delete=models.CASCADE)
    arrival_airfield = models.ForeignKey(Airfield, related_name='arrivals', on_delete=models.CASCADE)
    total_time = models.DecimalField(max_digits=5, decimal_places=2)
    pic_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sic_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    night_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    solo_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cross_country_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    day_takeoffs = models.IntegerField(default=0)
    day_landings = models.IntegerField(default=0)
    night_takeoffs = models.IntegerField(default=0)
    night_landings = models.IntegerField(default=0)
    actual_instrument_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    simulated_instrument_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pilot_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Flight on {self.date} with {self.aircraft}"
