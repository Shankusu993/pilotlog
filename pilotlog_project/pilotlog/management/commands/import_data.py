import json
from django.core.management.base import BaseCommand
from pilotlog.importers.aircraft_importer import AircraftImporter
from pilotlog.importers.airfield_importer import AirfieldImporter
from pilotlog.importers.pilot_importer import PilotImporter
from pilotlog.importers.flight_importer import FlightImporter

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file to import.')

    def handle(self, *args, **options):
        with open(options['json_file'], 'r') as f:
            data = json.load(f)

        importers = {
            'aircraft': AircraftImporter,
            'airfield': AirfieldImporter,
            'pilot': PilotImporter,
            'flight': FlightImporter,
        }

        # First pass: import Aircraft, Airfield, Pilot
        for record in data:
            table_name = record['table'].lower()
            if table_name in ['aircraft', 'airfield', 'pilot']:
                importer_class = importers.get(table_name)
                if importer_class:
                    importer = importer_class(record)
                    importer.process()

        # Second pass: import Flights
        for record in data:
            table_name = record['table'].lower()
            if table_name == 'flight':
                importer = FlightImporter(record)
                importer.process()

        self.stdout.write(self.style.SUCCESS('Successfully imported data.'))
