class BaseExporter:
    def __init__(self, queryset):
        self.queryset = queryset

    def export(self, file_path):
        raise NotImplementedError
