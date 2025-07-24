from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import import_data_task, export_data_task
from celery.result import AsyncResult


class ImportDataView(APIView):
    """
    API view to trigger the asynchronous import of data from a JSON file.
    """

    def post(self, request, *args, **kwargs):
        """
        Starts the import task.

        Args:
            request: The HTTP request object.

        Returns:
            A Response object with the task ID.
        """
        file_path = request.data.get("file_path")
        if not file_path:
            return Response(
                {"error": "file_path is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        task = import_data_task.delay(file_path)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)


class ExportDataView(APIView):
    """
    API view to trigger the asynchronous export of data to a CSV file.
    """

    def post(self, request, *args, **kwargs):
        """
        Starts the export task.

        Args:
            request: The HTTP request object.

        Returns:
            A Response object with the task ID.
        """
        file_path = request.data.get("file_path")
        if not file_path:
            return Response(
                {"error": "file_path is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        task = export_data_task.delay(file_path)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)


class TaskStatusView(APIView):
    """
    API view to check the status of a Celery task.
    """

    def get(self, request, task_id, *args, **kwargs):
        """
        Checks the status of a task.

        Args:
            request: The HTTP request object.
            task_id (str): The ID of the task to check.

        Returns:
            A Response object with the task status and result.
        """
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": str(task_result.result)
            if isinstance(task_result.result, Exception)
            else task_result.result,
        }
        return Response(result, status=status.HTTP_200_OK)
