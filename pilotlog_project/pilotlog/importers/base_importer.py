class BaseImporter:
    def __init__(self, record):
        self.record = record
        self.meta = record["meta"]
        self.guid = record["guid"]

    def process(self):
        raise NotImplementedError

    def get_model(self):
        raise NotImplementedError
