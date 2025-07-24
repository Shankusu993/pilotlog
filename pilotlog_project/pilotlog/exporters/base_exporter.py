class BaseExporter:
    """A base class for exporting data to a file."""

    def __init__(self, queryset):
        """
        Initializes the exporter with a queryset.

        Args:
            queryset: The Django queryset to be exported.
        """
        self.queryset = queryset

    def export(self, file_path):
        """
        Exports the queryset to a file.

        This method should be implemented by subclasses.

        Args:
            file_path (str): The path to the output file.
        """
        raise NotImplementedError
