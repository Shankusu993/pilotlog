import json
import logging
from django.core.management.base import BaseCommand
from pilotlog.importers.aircraft_importer import AircraftImporter
from pilotlog.importers.airfield_importer import AirfieldImporter
from pilotlog.importers.pilot_importer import PilotImporter
from pilotlog.importers.flight_importer import FlightImporter

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import data from JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file", type=str, help="The path to the JSON file to import."
        )

    def handle(self, *args, **options):
        with open(options["json_file"], "r") as f:
            data = json.load(f)

        importers = {
            "aircraft": AircraftImporter,
            "airfield": AirfieldImporter,
            "pilot": PilotImporter,
            "flight": FlightImporter,
        }

        logger.info("Starting import process...")

        # First pass: import Aircraft, Airfield, Pilot
        logger.info("Starting first pass: importing Aircraft, Airfield, and Pilot data...")
        for record in data:
            table_name = record["table"].lower()
            if table_name in ["aircraft", "airfield", "pilot"]:
                importer_class = importers.get(table_name)
                if importer_class:
                    try:
                        importer = importer_class(record)
                        importer.process()
                    except Exception as e:
                        logger.error(f"Error processing record {record['guid']}: {e}")

        # Second pass: import Flights
        logger.info("Starting second pass: importing Flight data...")
        for record in data:
            table_name = record["table"].lower()
            if table_name == "flight":
                try:
                    importer = FlightImporter(record)
                    importer.process()
                except Exception as e:
                    logger.error(f"Error processing record {record['guid']}: {e}")

        logger.info("Import process complete.")
