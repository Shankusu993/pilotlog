from celery import shared_task
from django.core.management import call_command


from django.conf import settings
import os

@shared_task
def import_data_task(file_path):
    abs_file_path = os.path.join(settings.BASE_DIR, '..', file_path)
    call_command("import_data", abs_file_path)


@shared_task
def export_data_task(file_path):
    abs_file_path = os.path.join(settings.BASE_DIR, '..', file_path)
    call_command("export_data", abs_file_path)
