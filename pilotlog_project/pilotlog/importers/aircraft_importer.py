from .base_importer import BaseImporter
from ..models import Aircraft


class AircraftImporter(BaseImporter):
    """Importer for aircraft data."""

    def get_model(self):
        """Returns the Aircraft model class."""
        return Aircraft

    def validate(self):
        """Validates the aircraft record."""
        if not self.meta.get("Model"):
            raise ValueError("Aircraft 'Model' is required.")
        return True

    def process(self):
        """Processes the aircraft record and saves it to the database."""
        if self.validate():
            self.get_model().objects.update_or_create(
                guid=self.guid,
                defaults={
                    "make": self.meta.get("Make"),
                    "model": self.meta.get("Model"),
                    "reference": self.meta.get("Reference"),
                    "fin": self.meta.get("Fin"),
                    "sea": self.meta.get("Sea", False),
                    "tmg": self.meta.get("TMG", False),
                    "efis": self.meta.get("Efis", False),
                    "fnpt": self.meta.get("FNPT"),
                    "run2": self.meta.get("Run2", False),
                    "aircraft_class": self.meta.get("Class"),
                    "power": self.meta.get("Power"),
                    "seats": self.meta.get("Seats"),
                    "active": self.meta.get("Active", True),
                    "kg5700": self.meta.get("Kg5700", False),
                    "rating": self.meta.get("Rating"),
                    "company": self.meta.get("Company"),
                    "complex": self.meta.get("Complex", False),
                    "condlog": self.meta.get("CondLog"),
                    "favlist": self.meta.get("FavList", False),
                    "category": self.meta.get("Category"),
                    "highperf": self.meta.get("HighPerf", False),
                    "submodel": self.meta.get("SubModel"),
                    "aerobatic": self.meta.get("Aerobatic", False),
                    "refsearch": self.meta.get("RefSearch"),
                    "tailwheel": self.meta.get("Tailwheel", False),
                    "defaultapp": self.meta.get("DefaultApp"),
                    "defaultlog": self.meta.get("DefaultLog"),
                    "defaultops": self.meta.get("DefaultOps"),
                    "devicecode": self.meta.get("DeviceCode"),
                    "aircraftcode": self.meta.get("AircraftCode"),
                    "defaultlaunch": self.meta.get("DefaultLaunch"),
                    "record_modified": self.meta.get("Record_Modified"),
                },
            )
