# Challenge 4

# Database Setup
In order to run this project, you will need an SQL Server database in Azure. You can create one on the [Azure Portal](https://portal.azure.com/) and create a new environment file in the project to register the database url (DB_URL), database user (DB_USER) and the password for that user (DB_PASSWORD).

## Installation
To run this project, first install the dependencies in a virtual environment. You can do so by executing the following commands in your terminal prompt with your virtual environment activated inside the python-challenge folder:
```
$ pip install -r requirements.txt
$ uvicorn src.app:app
```

## Features
Once the project is running, you can access the api documentation by entering http://localhost:8000/docs on your browser.