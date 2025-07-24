from django.db import models


class Aircraft(models.Model):
    """Represents an aircraft."""

    guid = models.CharField(max_length=255, unique=True)
    make = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    fin = models.CharField(max_length=255, null=True, blank=True)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(null=True, blank=True)
    run2 = models.BooleanField(default=False)
    aircraft_class = models.IntegerField(null=True, blank=True)
    power = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    complex = models.BooleanField(default=False)
    condlog = models.IntegerField(null=True, blank=True)
    favlist = models.BooleanField(default=False)
    category = models.IntegerField(null=True, blank=True)
    highperf = models.BooleanField(default=False)
    submodel = models.CharField(max_length=255, null=True, blank=True)
    aerobatic = models.BooleanField(default=False)
    refsearch = models.CharField(max_length=255, null=True, blank=True)
    tailwheel = models.BooleanField(default=False)
    defaultapp = models.IntegerField(null=True, blank=True)
    defaultlog = models.IntegerField(null=True, blank=True)
    defaultops = models.IntegerField(null=True, blank=True)
    devicecode = models.IntegerField(null=True, blank=True)
    aircraftcode = models.CharField(max_length=255, null=True, blank=True)
    defaultlaunch = models.IntegerField(null=True, blank=True)
    record_modified = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.reference or self.guid


class Airfield(models.Model):
    """Represents an airfield."""

    guid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    icao_code = models.CharField(max_length=4, null=True, blank=True)
    iata_code = models.CharField(max_length=3, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    afcat = models.IntegerField(null=True, blank=True)
    afcode = models.CharField(max_length=255, null=True, blank=True)
    afcountry = models.IntegerField(null=True, blank=True)
    notesuser = models.TextField(null=True, blank=True)
    regionuser = models.IntegerField(null=True, blank=True)
    elevationft = models.IntegerField(null=True, blank=True)
    record_modified = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name or self.guid


class Pilot(models.Model):
    """Represents a pilot."""

    guid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)
    favlist = models.BooleanField(default=False)
    userapi = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    pilotref = models.CharField(max_length=255, null=True, blank=True)
    pilotcode = models.CharField(max_length=255, null=True, blank=True)
    pilotphone = models.CharField(max_length=255, null=True, blank=True)
    certificate = models.CharField(max_length=255, null=True, blank=True)
    phonesearch = models.CharField(max_length=255, null=True, blank=True)
    pilotsearch = models.CharField(max_length=255, null=True, blank=True)
    rosteralias = models.CharField(max_length=255, null=True, blank=True)
    record_modified = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name or self.guid


class Flight(models.Model):
    """Represents a flight log entry."""

    guid = models.CharField(max_length=255, unique=True)
    aircraft = models.ForeignKey(
        Aircraft, to_field="guid", on_delete=models.SET_NULL, null=True, blank=True
    )
    departure_airfield = models.ForeignKey(
        Airfield,
        to_field="guid",
        related_name="departures",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    arrival_airfield = models.ForeignKey(
        Airfield,
        to_field="guid",
        related_name="arrivals",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    pilot1 = models.ForeignKey(
        Pilot,
        to_field="guid",
        related_name="flights_as_p1",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    pilot2 = models.ForeignKey(
        Pilot,
        to_field="guid",
        related_name="flights_as_p2",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    pilot3 = models.ForeignKey(
        Pilot,
        to_field="guid",
        related_name="flights_as_p3",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    pilot4 = models.ForeignKey(
        Pilot,
        to_field="guid",
        related_name="flights_as_p4",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    flight_date = models.DateField(null=True, blank=True)
    total_duration = models.IntegerField(help_text="In minutes", null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    pf = models.BooleanField(default=False)
    pax = models.IntegerField(null=True, blank=True)
    fuel = models.FloatField(null=True, blank=True)
    deice = models.BooleanField(default=False)
    route = models.CharField(max_length=255, null=True, blank=True)
    today = models.IntegerField(null=True, blank=True)
    minu1 = models.IntegerField(null=True, blank=True)
    minu2 = models.IntegerField(null=True, blank=True)
    minu3 = models.IntegerField(null=True, blank=True)
    minu4 = models.IntegerField(null=True, blank=True)
    minxc = models.IntegerField(null=True, blank=True)
    arrrwy = models.CharField(max_length=255, null=True, blank=True)
    deprwy = models.CharField(max_length=255, null=True, blank=True)
    ldgday = models.IntegerField(null=True, blank=True)
    liftsw = models.IntegerField(null=True, blank=True)
    report = models.CharField(max_length=255, null=True, blank=True)
    tagops = models.CharField(max_length=255, null=True, blank=True)
    toedit = models.BooleanField(default=False)
    minair = models.IntegerField(null=True, blank=True)
    mincop = models.IntegerField(null=True, blank=True)
    minifr = models.IntegerField(null=True, blank=True)
    minimt = models.IntegerField(null=True, blank=True)
    minpic = models.IntegerField(null=True, blank=True)
    minrel = models.IntegerField(null=True, blank=True)
    minsfr = models.IntegerField(null=True, blank=True)
    dateutc = models.CharField(max_length=255, null=True, blank=True)
    hobbsin = models.FloatField(null=True, blank=True)
    holding = models.IntegerField(null=True, blank=True)
    pairing = models.CharField(max_length=255, null=True, blank=True)
    signbox = models.IntegerField(null=True, blank=True)
    tonight = models.IntegerField(null=True, blank=True)
    usernum = models.IntegerField(null=True, blank=True)
    mindual = models.IntegerField(null=True, blank=True)
    minexam = models.IntegerField(null=True, blank=True)
    crewlist = models.CharField(max_length=255, null=True, blank=True)
    datebase = models.CharField(max_length=255, null=True, blank=True)
    fuelused = models.FloatField(null=True, blank=True)
    hobbsout = models.FloatField(null=True, blank=True)
    ldgnight = models.IntegerField(null=True, blank=True)
    nextpage = models.BooleanField(default=False)
    tagdelay = models.CharField(max_length=255, null=True, blank=True)
    training = models.CharField(max_length=255, null=True, blank=True)
    userbool = models.BooleanField(default=False)
    usertext = models.CharField(max_length=255, null=True, blank=True)
    mininstr = models.IntegerField(null=True, blank=True)
    minnight = models.IntegerField(null=True, blank=True)
    minpicus = models.IntegerField(null=True, blank=True)
    mintotal = models.IntegerField(null=True, blank=True)
    arroffset = models.IntegerField(null=True, blank=True)
    datelocal = models.CharField(max_length=255, null=True, blank=True)
    depoffset = models.IntegerField(null=True, blank=True)
    taglaunch = models.CharField(max_length=255, null=True, blank=True)
    taglesson = models.CharField(max_length=255, null=True, blank=True)
    totimeutc = models.IntegerField(null=True, blank=True)
    arrtimeutc = models.IntegerField(null=True, blank=True)
    baseoffset = models.IntegerField(null=True, blank=True)
    deptimeutc = models.IntegerField(null=True, blank=True)
    ldgtimeutc = models.IntegerField(null=True, blank=True)
    fuelplanned = models.FloatField(null=True, blank=True)
    nextsummary = models.BooleanField(default=False)
    tagapproach = models.CharField(max_length=255, null=True, blank=True)
    arrtimesched = models.IntegerField(null=True, blank=True)
    deptimesched = models.IntegerField(null=True, blank=True)
    flightnumber = models.CharField(max_length=255, null=True, blank=True)
    flightsearch = models.CharField(max_length=255, null=True, blank=True)
    record_modified = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.guid
