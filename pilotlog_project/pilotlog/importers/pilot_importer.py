from .base_importer import BaseImporter
from ..models import Pilot


class PilotImporter(BaseImporter):
    """Importer for pilot data."""

    def get_model(self):
        """Returns the Pilot model class."""
        return Pilot

    def process(self):
        """Processes the pilot record and saves it to the database."""
        self.get_model().objects.update_or_create(
            guid=self.guid,
            defaults={
                "name": self.meta.get("PilotName"),
                "email": self.meta.get("PilotEMail"),
                "company": self.meta.get("Company"),
                "active": self.meta.get("Active", True),
                "notes": self.meta.get("Notes"),
                "favlist": self.meta.get("FavList", False),
                "userapi": self.meta.get("UserAPI"),
                "facebook": self.meta.get("Facebook"),
                "linkedin": self.meta.get("LinkedIn"),
                "pilotref": self.meta.get("PilotRef"),
                "pilotcode": self.meta.get("PilotCode"),
                "pilotphone": self.meta.get("PilotPhone"),
                "certificate": self.meta.get("Certificate"),
                "phonesearch": self.meta.get("PhoneSearch"),
                "pilotsearch": self.meta.get("PilotSearch"),
                "rosteralias": self.meta.get("RosterAlias"),
                "record_modified": self.meta.get("Record_Modified"),
            },
        )
