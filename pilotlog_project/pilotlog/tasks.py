from celery import shared_task
from django.core.management import call_command


@shared_task
def import_data_task(file_path):
    call_command("import_data", file_path)


@shared_task
def export_data_task(file_path):
    call_command("export_data", file_path)
