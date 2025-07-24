class BaseImporter:
    """A base class for importing data from a dictionary."""

    def __init__(self, record):
        """
        Initializes the importer with a single record.

        Args:
            record (dict): A dictionary representing a single record from the
                import file.
        """
        self.record = record
        self.meta = record["meta"]
        self.guid = record["guid"]

    def validate(self):
        """
        Validates the record.

        This method should be implemented by subclasses.
        """
        raise NotImplementedError

    def process(self):
        """
        Processes the record and saves it to the database.

        This method should be implemented by subclasses.
        """
        raise NotImplementedError

    def get_model(self):
        """
        Returns the Django model class that this importer handles.

        This method should be implemented by subclasses.
        """
        raise NotImplementedError
