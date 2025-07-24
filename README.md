# User Documentation

This document provides instructions on how to set up and use the Pilot Log application's importer and exporter modules.

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

4.  **Database Setup:**
    Run the following commands from the `pilotlog_project` directory to create the database and apply the schema:
    ```bash
    python manage.py makemigrations pilotlog
    python manage.py migrate
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
