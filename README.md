# PyDBControl

A Python library to control, manage, and compare PostgreSQL tables with ease. Designed for robust database automation, schema validation, and table comparison, PyDBControl is ideal for ETL, data validation, and database testing workflows.

## Features

- **Automated Table Creation**: Create tables from SQL model files and insert valid sample data automatically, respecting all column constraints (e.g., `CHECK`, `IN`, `BETWEEN`, `PRIMARY KEY`).
- **Dynamic Primary Key Detection**: Handles tables with any primary key name, not just `id`.
- **Constraint-Aware Data Generation**: Generates compliant random data for each table and row, matching all SQL constraints.
- **Comprehensive Logging**: All actions (table creation, row insertion, comparison, errors) are logged to a file for full auditability.
- **Table Comparison**: Compare multiple tables (even with different schemas) and get detailed differences, with warnings for column mismatches.
- **Schema Validation**: Store and validate table schemas to detect changes or drifts over time.
- **Modular Design**: Core classes for DB connection, table management, comparison, logging, and utilities.
- **Example Scripts**: Ready-to-use examples for table creation, data insertion, and table comparison.

## System Overview

PyDBControl is organized into several core modules:

- `pydbcontrol/db_connector.py`: Manages PostgreSQL connections and query execution. Supports logging.
- `pydbcontrol/table_manager.py`: Handles table creation, row insertion, and CRUD operations. Detects primary keys dynamically. Supports logging.
- `pydbcontrol/comparator.py`: Compares tables by key column, reports differences, and logs warnings for schema mismatches.
- `pydbcontrol/logger.py`: Logs all actions and errors to a file. Used by all other modules.
- `pydbcontrol/utils.py`: Stores and validates table schemas, with logging support.
- `model/`: Contains SQL files defining your database tables.
- `examples/`: Example scripts for creating tables, inserting data, and comparing tables.

## Example Usage

### 1. Create All Tables and Insert Sample Data

```python
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.table_manager import TableManager
from pydbcontrol.logger import Logger
import os

logger = Logger('pydbcontrol.log')
db = DBConnector(logger=logger)
db.connect()
model_dir = './model'
sql_files = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if f.endswith('.sql')]
for sql_path in sql_files:
    table_name = ... # extract from SQL file
    tm = TableManager(db, table_name, logger=logger)
    tm.table_creator(sql_path)
    # Insert sample rows as shown in examples/create_full_database.py

db.disconnect()
```

### 2. Compare Tables

```python
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.comparator import Comparator
from pydbcontrol.logger import Logger

logger = Logger('pydbcontrol.log')
db = DBConnector(logger=logger)
db.connect()
comp = Comparator(db, logger=logger)
diff = comp.compare_tables('table1', 'table2', key_column='id')
print(diff)
db.disconnect()
```

### 3. Validate Table Schema

```python
from pydbcontrol.db_connector import DBConnector
from pydbcontrol.utils import Utils
from pydbcontrol.logger import Logger

logger = Logger('pydbcontrol.log')
db = DBConnector(logger=logger)
db.connect()
Utils.store_initial_schema(db, 'my_table', logger=logger)
Utils.validate_schema(db, 'my_table', logger=logger)
db.disconnect()
```

## Installation

```bash
pip install -r requirements.txt
```

## Requirements
- Python 3.7+
- PostgreSQL database
- See `requirements.txt` for Python dependencies

## Logging
All actions and errors are logged to `pydbcontrol.log` by default. You can change the log file name when initializing the `Logger`.

## How to Package and Distribute PyDBControl as a Python Library

Follow these steps to turn this project into a reusable Python library that can be installed via pip, shared on PyPI, or used in other projects:

### 1. Organize Your Project Structure

Your project should look like this:

```
TUBITAK-UZAY-PyDBControl/
├── pydbcontrol/           # Main package code (with __init__.py)
├── examples/              # Example scripts (not included in package)
├── model/                 # SQL model files (optional, not in package)
├── schemas/               # Schema files (optional)
├── tests/                 # Unit tests
├── setup.py               # Packaging configuration
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── ...
```

### 2. Ensure `__init__.py` Exists

Make sure there is an `__init__.py` file in the `pydbcontrol` directory. This makes it a Python package.

### 3. Update `setup.py`

Your `setup.py` should already be configured (see above). Make sure:
- `packages=find_packages() OR packages=["pydbcontrol"]` includes your main package.
- `install_requires` lists all dependencies.
- Metadata (author, description, etc.) is correct.

### 4. (Optional) Add a `pyproject.toml`

For modern packaging, you can add a `pyproject.toml` for build system requirements:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

### 5. Build the Package

From the project root, run:

```bash
python setup.py sdist bdist_wheel
```

This will create `dist/pydbcontrol-<version>.tar.gz` and `.whl` files.

### 6. Test the Package Locally

Install your package in a virtual environment to test:

```bash
pip install dist/pydbcontrol-<version>-py3-none-any.whl
```

Then try importing it in Python:

```python
from pydbcontrol.db_connector import DBConnector
```

### 7. (Optional) Publish to PyPI

1. Register on [PyPI](https://pypi.org/).
2. Install Twine:
   ```bash
   pip install twine
   ```
3. Upload your package:
   ```bash
   twine upload dist/*
   ```

### 8. Use in Other Projects

If the library is local (not published to PyPI), install directly from the wheel file:

```bash
pip install /path/to/pydbcontrol-0.1.0-py3-none-any.whl
```

After publishing, install with:

```bash
pip install pydbcontrol
```

Or, for local development, use:

```bash
pip install -e .
```

### 9. Versioning and Updates

- Update the `version` in `setup.py` for each release.
- Tag releases in git for best practice.

### 10. Documentation

- Keep `README.md` up to date.
- Optionally, add docstrings and use tools like Sphinx for API docs.

---

With these steps, PyDBControl will be a reusable, installable Python library/package ready for use in any project or for public distribution!

## License
MIT

## Author
Ediz Arkin Kobak

## Project URL
https://github.com/EdizArkin/TUBITAK-UZAY-PyDBControl
