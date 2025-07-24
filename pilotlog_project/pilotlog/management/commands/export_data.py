import logging
from django.core.management.base import BaseCommand
from pilotlog.models import Flight
from pilotlog.exporters.csv_logbook_exporter import CsvLogbookExporter

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Export data to a specified format"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="The path to the output file.")
        parser.add_argument(
            "--format", type=str, default="csv_logbook", help="The format to export to."
        )

    def handle(self, *args, **options):
        format = options["format"]
        file_path = options["file_path"]

        exporters = {
            "csv_logbook": CsvLogbookExporter,
        }

        exporter_class = exporters.get(format)
        if not exporter_class:
            logger.error(f"Unknown format: {format}")
            return

        logger.info(f"Exporting data to {file_path} in {format} format...")
        queryset = Flight.objects.all()
        exporter = exporter_class(queryset)
        try:
            exporter.export(file_path)
            logger.info(f"Successfully exported data to {file_path} in {format} format.")
            
        except Exception as e:
            logger.error(f"Error exporting data: {e}")
