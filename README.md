# Pilot Log

This is a Django application for importing and exporting pilot logbook data.

## Setup

1.  **Prerequisites:**

    - Python 3.9 or higher
    - Conda (or another virtual environment manager)

2.  **Create and Activate Conda Environment:**

    ```bash
    conda create --name pilotlog python=3.9 -y
    conda activate pilotlog
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create `.env` file:**
    Create a `.env` file in the root of the project and add the following line:

    ```
    SECRET_KEY='your-secret-key'
    ```

5.  **Database Setup:**
    Run the following commands from the `pilotlog_project` directory to create the database and apply the schema:

    ```bash
    python manage.py makemigrations pilotlog
    python manage.py migrate
    ```

6.  **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7.  **Run the Celery Worker:**
    In a separate terminal, run the following command from the `pilotlog_project` directory:
    ```bash
    celery -A pilotlog_project worker -l info
    ```

## Usage

### Importer

The `import_data` management command is used to import data from a JSON file into the database.

**Command:**

```bash
python manage.py import_data <path_to_json_file>
```

**Example:**
To import data from the `import - pilotlog_mcc.json` file located in the `data` directory, run the following command from the `pilotlog_project` directory:

```bash
python manage.py import_data ../data/import\ -\ pilotlog_mcc.json
```

The command will parse the JSON file and populate the `Aircraft`, `Airfield`, `Pilot`, and `Flight` tables in the database.

### Exporter

The `export_data` management command is used to export data from the database to a CSV file.

**Command:**

```bash
python manage.py export_data <path_to_csv_file>
```

**Example:**
To export the data to a file named `exported_logbook.csv` in the `data` directory, run the following command from the `pilotlog_project` directory:

```bash
python manage.py export_data ../data/exported_logbook.csv
```

The command will generate a CSV file with the `Aircraft` and `Flight` data in the format specified by the `export-logbook_template.csv` file.

## Testing

To run the test suite, run the following command from the `pilotlog_project` directory:

```bash
python manage.py test pilotlog
```

## API Usage

The application exposes a set of APIs for triggering the import and export processes asynchronously.

### Start an Import

To start an import, send a POST request to the `/api/import/` endpoint with the path to the JSON file:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"file_path": "data/import - pilotlog_mcc.json"}' http://localhost:8000/api/import/
```

This will return a task ID, which you can use to check the status of the import.

### Start an Export

To start an export, send a POST request to the `/api/export/` endpoint with the desired output file path:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"file_path": "data/exported_logbook.csv"}' http://localhost:8000/api/export/
```

### Check Task Status

To check the status of a task, send a GET request to the `/api/task/<task_id>/` endpoint:

```bash
curl http://localhost:8000/api/task/<task_id>/
```

## Conventions and Best Practices

This project follows a number of best practices to ensure code quality, maintainability, and scalability.

- **Modular Design:** The application is designed with a modular architecture. The importer and exporter logic is encapsulated in separate classes, making the code easy to understand, maintain, and extend.
- **Normalized Data Model:** The data is stored in a normalized SQL schema, which ensures data integrity and avoids redundancy.
- **Testing:** The project has a comprehensive test suite that covers the core functionality of the application. This helps to prevent regressions and ensure that the application is working as expected.
- **Logging:** The application uses Python's built-in logging module to provide detailed information about the import and export processes.
- **Configuration Management:** Sensitive information, such as the `SECRET_KEY`, is loaded from an environment variable, which is a security best practice.
- **Code Formatting and Linting:** The codebase is formatted with `black` and linted with `flake8` to ensure a consistent style and to identify potential bugs.
- **Automated Documentation:** The project uses `Sphinx` to automatically generate documentation from the docstrings in the code.
