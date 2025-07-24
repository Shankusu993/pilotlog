from .base_importer import BaseImporter
from ..models import Airfield


class AirfieldImporter(BaseImporter):
    """Importer for airfield data."""

    def get_model(self):
        """Returns the Airfield model class."""
        return Airfield

    def process(self):
        """Processes the airfield record and saves it to the database."""
        self.get_model().objects.update_or_create(
            guid=self.guid,
            defaults={
                "name": self.meta.get("AFName"),
                "icao_code": self.meta.get("AFICAO"),
                "iata_code": self.meta.get("AFIATA"),
                "latitude": self.meta.get("Latitude"),
                "longitude": self.meta.get("Longitude"),
                "afcat": self.meta.get("AFCat"),
                "afcode": self.meta.get("AFCode"),
                "afcountry": self.meta.get("AFCountry"),
                "notesuser": self.meta.get("NotesUser"),
                "regionuser": self.meta.get("RegionUser"),
                "elevationft": self.meta.get("ElevationFT"),
                "record_modified": self.meta.get("Record_Modified"),
            },
        )
