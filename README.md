## How to run the django project

```
poetry install
poetry run python manage.py migrate --noinput
poetry run python manage.py initadmin admin admin@example.com admin8420
poetry run python manage.py runserver
```

Now you can access the admin portal at `127.0.0.1:8000/admin` with username `admin` and password `admin8420`

## Set Up Your Dev Environment

### Install Poetry

To install Poetry, you can follow these steps:

1. First, you need to have Python 3.6 or higher installed on your system. You can check if you have Python installed by running the command `python --version` in your terminal. If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

2. Next, you can install Poetry by running the following command in your terminal:

   ```bash
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

3. Once the installation is complete, you can check that Poetry is installed by running the command `poetry --version` in your terminal. This should output the version of Poetry that you have installed.

4. Finally, you can start using Poetry to manage your Python dependencies by navigating to your project directory and running the command `poetry init`. This will create a `pyproject.toml` file in your project directory, which you can use to define your project's dependencies.

5. You can then use the `poetry add` command to add dependencies to your project. For example, to add the `requests` library, you can run the command `poetry add requests`.

### Install Dependency

To install dependency, execute the following command:

```bash
poetry install
```

### Activate/Exit the virtual environment you just installed

To activate:

```bash
    poetry shell
```

To deactivate:

```bash
    exit
```
