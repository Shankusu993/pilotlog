from celery import shared_task
from django.core.management import call_command


from django.conf import settings
import os

@shared_task(bind=True)
def import_data_task(self, file_path):
    try:
        abs_file_path = os.path.join(settings.BASE_DIR, "..", file_path)
        call_command("import_data", abs_file_path)
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc_type': type(e).__name__, 'exc_message': str(e)})
        raise e


@shared_task(bind=True)
def export_data_task(self, file_path):
    try:
        abs_file_path = os.path.join(settings.BASE_DIR, "..", file_path)
        call_command("export_data", abs_file_path)
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc_type': type(e).__name__, 'exc_message': str(e)})
        raise e
