from django.urls import path
from .api import ImportDataView, ExportDataView, TaskStatusView

urlpatterns = [
    path("import/", ImportDataView.as_view(), name="import_data"),
    path("export/", ExportDataView.as_view(), name="export_data"),
    path("task/<str:task_id>/", TaskStatusView.as_view(), name="task_status"),
]
