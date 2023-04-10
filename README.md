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

## How to run the django project

We use `docker` to manage the project. To run this project, ensure that `docker` is installed and configured correctly.

1. Ensure that there is a folder called `watchmate_db` in your `$HOME` directory.
2. Grant permission to the `watchmate_db` folder to ensure that it can be accessed by `docker`. To simplify, you can set it to `777`.
3. Execute `docker compose up --build` to start the project.
4. Access the admin portal by visiting `127.0.0.1/admin` using `admin` as the username and `admin8420` as the password.
5. The data created by this project will be stored in the `watchmate_db` folder located in your `$HOME` directory.
