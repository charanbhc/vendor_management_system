# Vendor Management System

## Introduction
The Vendor Management System is a Django-based web application that allows you to manage vendors and purchase orders efficiently. It includes CRUD operations and performance metrics for vendors.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (3.11 or later)
- Django (4.x)
- Django REST Framework (3.x)
- Git

## Installation
1. **Clone the repository**:
    ```shell
    git clone https://github.com/charanbhc/vendor_management_system.git
    cd vendor_management_system
    ```

2. **Create a virtual environment** (optional but recommended):
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```shell
    pip install -r requirements.txt
    ```

## Configuration
- **Database**: Update the `DATABASES` setting in `settings.py` to configure your database. By default, it uses SQLite.
- **Other settings**: Adjust other settings as needed (e.g., secret key, debug mode).

## Running the Application
1. **Apply migrations**:
    ```shell
    python manage.py migrate
    ```

2. **Start the server**:
    ```shell
    python manage.py runserver
    ```

3. Access the application at `http://localhost:8000`.

## Running Tests
To run the tests, use the following command:
```shell
python manage.py test vendor_app


You should see the test results in the console.

Contributing
Contributions are welcome! Please check out the CONTRIBUTING file for guidelines on how to contribute.

License
This project is licensed under the MIT License. See the LICENSE file for details.


This README structure provides a clear guide for users to understand your project, how to set it up, and how to test it. Make sure to customize the content to fit your specific project requirements.


## Running Tests
To run the test suite for the application, follow these steps:

1. **Activate the virtual environment** (if you're using one):
    ```shell
    source venv/bin/activate
    ```

2. **Ensure that you have all the dependencies installed**:
    Make sure you've run the installation command:
    ```shell
    pip install -r requirements.txt
    ```

3. **Run the test suite**:
    Use the following command in the root of the project directory:
    ```shell
    python manage.py test
    ```

    This command runs the Django test suite, which includes the tests in the `vendor_app` app as well as any other apps you've included.

4. **Review the output**:
    Check the console output for any test failures or errors. If all tests pass, you should see a message indicating that the tests completed successfully.

If you encounter any errors, review the test cases and application code to identify and resolve the issues.

For more information on writing and running tests in Django, see the [Django documentation](https://docs.djangoproject.com/en/stable/topics/testing/).
