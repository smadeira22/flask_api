# Crypto Currencies RESTful API


## Installation and Usage

1. Open your terminal

2. On the terminal do the following:

- Create a new folder
    - Type `mkdir [folder name]`

- Open new folder  
    - Type `cd [folder name]`

- Clone repo onto your machine
    - Type `git clone [repo_link]`

- Open repository 
    - Type `cd [repo_name].git`

- Create flask.env file
    - Type `touch flask.env`
    - add `FLASK_DEBUG=1`

- Set up database
    - create an elephant sql instace by following the link: `https://www.elephantsql.com/`
    - update models.py file to app.config['SQLALCHEMY_DATABASE_URI'] = `postgresql=[sql_instance]`

-To install dependencies type the following:
    - Type `pip install pipenv`
    - Type `pipenv install`
    - Type `pipenv shell`

-To seed database
    - type `python seed.py`

-To run local host
    -type `python app.py`
    -local host will run on 4000

## Endpoints

-  "GET /",
    -   "GET /cryptoCurrencies",
    -    "GET /cryptoCurrencies/<int:id>",
    -    "POST /cryptoCurrencies",
    -    "PATCH /cryptoCurrencies/<int:id>",
    -    "DELETE /cryptoCurrencies/<int:id>"

## Technologies
- Flask
- Python
- Pipenv
