# Django App for Supply Chain Insights' Data Models and API 
1. Clone this repo on the same path as where you have the `manage.py` file for your Django Project 
2. By default this Django app is called 'scip' -- Install the app in your Django project settings in the file named `settings.py` 

# Data Migration Scripts 
* Scripts for migrating data into the database live in `scip/management/commands` folder 
* Data is being migrated by calling a new API wrapper (which you can find code for in `supply_chain_apis` repo) 

# API Docs 

* The API is create using the Django REST Framework toolkit, called `djangorestframework` library in the settings 

* Queries for endpoints are defined in `views.py` and endpoint urls are defined in `scip/urls.py`

* API endpoints at `/api`
* API Swagger Docs at `/api-docs` 

# Database Architecture 

# System Architecture 
