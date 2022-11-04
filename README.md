# Django-challenge
## Stack
 1. Django 3.2.7
 2. Python 3.6.8
 3. MySQL  Ver 14.14 Distrib 5.7.32

## GETTING STARTED
### Create virtualenv
```
pip install virtualenv
virtualenv -p /path/to/python3.6 virtualenv
```
or
```
sudo apt install python3.6-venv
python3.6 -m venv /path/to/new/virtual/environment
virtualenv -p /path/to/python3.6 virtualenv
```
### Install requirements
```
pip install -r requirements/base.txt
```
### Create .env file
A _.env.example_ file can be found in *oowlish_challenge/.env.example*. This file shows env variables to set for settings in order to run project. For that purpose it was used [python-decouple](https://github.com/henriquebastos/python-decouple) package.
Fill variables with your own then, on **_oowlish_challenge/_** folder, copy *.env.example* file
```
cp .env.example .env
```
### Database
Once you have defined database settings in _.env_ file, then you have to run django migrations.
```
python oowlish_challenge/manage.py migrate
```
### Customers
In order to start testing the project, it's necesary to create some customers. It's possible to upload a CSV file with customers data from the admin. Just go to the *Customers* app and click on the button in the upper right corner.

The file must to have the next columns:

| id  |  first_name  |  last_name  |  email  |  gender  |  company  |  city  |  title
|-----|--------------|-------------|---------|----------|-----------|--------|-------|

The function will return the values with the customers location and save the data to the model.

or

This project has a fixture file for that purpose.

To load data from fixtures:
```
python manage.py loaddata customers/fixtures/customers.json
```
### Run project
Once you have finished previous steps you can run project on local environment.
```
python oowlish_challenge/manage.py runserver
```
### API's
-  **{{host}}/api/customers/** listing all the customers.
-  **{{host}}/api/customers-by-id/** get a single customer by id.

### Notes:
This project needs Google API Key to load the customers location. It's necessary to add your key to the *.env* file.  It is recommended to restrict the API key.  To do this, read the next [Google documentation](https://developers.google.com/maps/documentation/javascript/get-api-key#restrict_key)
