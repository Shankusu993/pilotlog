from django.test import TestCase
from pilotlog.models import Aircraft, Airfield, Pilot, Flight
from pilotlog.importers.aircraft_importer import AircraftImporter
from pilotlog.importers.airfield_importer import AirfieldImporter
from pilotlog.importers.pilot_importer import PilotImporter
from pilotlog.importers.flight_importer import FlightImporter


class AircraftImporterTestCase(TestCase):
    def test_aircraft_importer(self):
        record = {
            "user_id": 125880,
            "table": "Aircraft",
            "guid": "00000000-0000-0000-0000-000000000367",
            "meta": {
                "Fin": "",
                "Sea": False,
                "TMG": False,
                "Efis": False,
                "FNPT": 0,
                "Make": "Cessna",
                "Run2": False,
                "Class": 5,
                "Model": "C150",
                "Power": 1,
                "Seats": 0,
                "Active": True,
                "Kg5700": False,
                "Rating": "",
                "Company": "Other",
                "Complex": False,
                "CondLog": 69,
                "FavList": False,
                "Category": 1,
                "HighPerf": False,
                "SubModel": "",
                "Aerobatic": False,
                "RefSearch": "PHALI",
                "Reference": "PH-ALI",
                "Tailwheel": False,
                "DefaultApp": 0,
                "DefaultLog": 2,
                "DefaultOps": 0,
                "DeviceCode": 1,
                "AircraftCode": "00000000-0000-0000-0000-000000000367",
                "DefaultLaunch": 0,
                "Record_Modified": 1616320991,
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = AircraftImporter(record)
        importer.process()

        self.assertEqual(Aircraft.objects.count(), 1)
        aircraft = Aircraft.objects.first()
        self.assertEqual(aircraft.make, "Cessna")
        self.assertEqual(aircraft.model, "C150")
        self.assertEqual(aircraft.reference, "PH-ALI")

    def test_aircraft_importer_missing_model(self):
        record = {
            "user_id": 125880,
            "table": "Aircraft",
            "guid": "00000000-0000-0000-0000-000000000367",
            "meta": {
                "Make": "Cessna",
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = AircraftImporter(record)
        with self.assertRaises(ValueError):
            importer.process()


class AirfieldImporterTestCase(TestCase):
    def test_airfield_importer(self):
        record = {
            "user_id": 125880,
            "table": "Airfield",
            "guid": "00000000-0000-0000-0000-000000040048",
            "meta": {
                "AFCat": 8,
                "AFCode": "00000000-0000-0000-0000-000000040048",
                "AFIATA": "NKT",
                "AFICAO": "LTCV",
                "AFName": "Sirnak Serafettin Elci",
                "TZCode": 333,
                "Latitude": 37218,
                "ShowList": False,
                "AFCountry": 223,
                "Longitude": -42036,
                "NotesUser": "ATIS 128.400",
                "RegionUser": 0,
                "ElevationFT": 0,
                "Record_Modified": 1616320991,
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = AirfieldImporter(record)
        importer.process()

        self.assertEqual(Airfield.objects.count(), 1)
        airfield = Airfield.objects.first()
        self.assertEqual(airfield.name, "Sirnak Serafettin Elci")
        self.assertEqual(airfield.icao_code, "LTCV")
        self.assertEqual(airfield.iata_code, "NKT")

    def test_airfield_importer_missing_name(self):
        record = {
            "user_id": 125880,
            "table": "Airfield",
            "guid": "00000000-0000-0000-0000-000000040048",
            "meta": {
                "AFICAO": "LTCV",
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = AirfieldImporter(record)
        with self.assertRaises(ValueError):
            importer.process()


class PilotImporterTestCase(TestCase):
    def test_pilot_importer(self):
        record = {
            "user_id": 125880,
            "table": "Pilot",
            "guid": "00000000-0000-0000-0000-000000000001",
            "meta": {
                "Notes": "",
                "Active": True,
                "Company": "Turkish Airlines",
                "FavList": True,
                "UserAPI": "",
                "Facebook": "",
                "LinkedIn": "",
                "PilotRef": "080648",
                "PilotCode": "00000000-0000-0000-0000-000000000001",
                "PilotName": "SELF",
                "PilotEMail": "",
                "PilotPhone": "",
                "Certificate": "",
                "PhoneSearch": "",
                "PilotSearch": "SELF",
                "RosterAlias": "",
                "Record_Modified": 1616320991,
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = PilotImporter(record)
        importer.process()

        self.assertEqual(Pilot.objects.count(), 1)
        pilot = Pilot.objects.first()
        self.assertEqual(pilot.name, "SELF")
        self.assertEqual(pilot.company, "Turkish Airlines")

    def test_pilot_importer_missing_name(self):
        record = {
            "user_id": 125880,
            "table": "Pilot",
            "guid": "00000000-0000-0000-0000-000000000001",
            "meta": {
                "Company": "Turkish Airlines",
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = PilotImporter(record)
        with self.assertRaises(ValueError):
            importer.process()


class FlightImporterTestCase(TestCase):
    def setUp(self):
        Aircraft.objects.create(
            guid="00000000-0000-0000-0000-000000000367",
            make="Cessna",
            model="C150",
            reference="PH-ALI",
        )
        Airfield.objects.create(
            guid="00000000-0000-0000-0000-000000009693",
            name="LEY",
            icao_code="EHLE",
        )
        Pilot.objects.create(
            guid="00000000-0000-0000-0000-000000000001",
            name="SELF",
        )

    def test_flight_importer(self):
        record = {
            "user_id": 125880,
            "table": "Flight",
            "guid": "00000000-0000-0000-0000-000000009218",
            "meta": {
                "PF": True,
                "Pax": 0,
                "Fuel": 0,
                "DeIce": False,
                "Route": "",
                "ToDay": 1,
                "minU1": 0,
                "minU2": 0,
                "minU3": 0,
                "minU4": 0,
                "minXC": 0,
                "ArrRwy": "",
                "DepRwy": "",
                "LdgDay": 1,
                "LiftSW": 0,
                "P1Code": "00000000-0000-0000-0000-000000000001",
                "P2Code": "00000000-0000-0000-0000-000000000000",
                "P3Code": "00000000-0000-0000-0000-000000000000",
                "P4Code": "00000000-0000-0000-0000-000000000000",
                "Report": "",
                "TagOps": "",
                "ToEdit": False,
                "minAIR": 0,
                "minCOP": 0,
                "minIFR": 0,
                "minIMT": 0,
                "minPIC": 0,
                "minREL": 0,
                "minSFR": 0,
                "ArrCode": "00000000-0000-0000-0000-000000009693",
                "DateUTC": "1998-03-16",
                "DepCode": "00000000-0000-0000-0000-000000009693",
                "HobbsIn": 0,
                "Holding": 0,
                "Pairing": "",
                "Remarks": "intro C150 keurig",
                "SignBox": 0,
                "ToNight": 0,
                "UserNum": 0,
                "minDUAL": 60,
                "minEXAM": 0,
                "CrewList": "",
                "DateBASE": "1998-03-15",
                "FuelUsed": 0,
                "HobbsOut": 0,
                "LdgNight": 0,
                "NextPage": False,
                "TagDelay": "",
                "Training": "",
                "UserBool": False,
                "UserText": "",
                "minINSTR": 0,
                "minNIGHT": 0,
                "minPICUS": 0,
                "minTOTAL": 60,
                "ArrOffset": 60,
                "DateLOCAL": "1998-03-16",
                "DepOffset": 60,
                "TagLaunch": "",
                "TagLesson": "",
                "ToTimeUTC": 0,
                "ArrTimeUTC": 0,
                "BaseOffset": -99,
                "DepTimeUTC": 0,
                "FlightCode": "00000000-0000-0000-0000-000000009218",
                "LdgTimeUTC": 0,
                "FuelPlanned": 0,
                "NextSummary": False,
                "TagApproach": "",
                "AircraftCode": "00000000-0000-0000-0000-000000000367",
                "ArrTimeSCHED": 0,
                "DepTimeSCHED": 0,
                "FlightNumber": "",
                "FlightSearch": "19980316:LEYLEY",
                "Record_Modified": 1616320991,
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = FlightImporter(record)
        importer.process()

        self.assertEqual(Flight.objects.count(), 1)
        flight = Flight.objects.first()
        self.assertEqual(flight.remarks, "intro C150 keurig")
        self.assertEqual(flight.aircraft.reference, "PH-ALI")
        self.assertEqual(flight.departure_airfield.name, "LEY")
        self.assertEqual(flight.pilot1.name, "SELF")

    def test_flight_importer_missing_date(self):
        record = {
            "user_id": 125880,
            "table": "Flight",
            "guid": "00000000-0000-0000-0000-000000009218",
            "meta": {
                "AircraftCode": "00000000-0000-0000-0000-000000000367",
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = FlightImporter(record)
        with self.assertRaises(ValueError):
            importer.process()

    def test_flight_importer_missing_aircraft(self):
        record = {
            "user_id": 125880,
            "table": "Flight",
            "guid": "00000000-0000-0000-0000-000000009218",
            "meta": {
                "DateUTC": "1998-03-16",
            },
            "platform": 9,
            "_modified": 1616317613,
        }

        importer = FlightImporter(record)
        with self.assertRaises(ValueError):
            importer.process()
