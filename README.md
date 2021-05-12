
[![CircleCI](https://circleci.com/gh/thoth-ky/currency_exhange_app.svg?style=svg)](https://app.circleci.com/pipelines/github/thoth-ky/currency_exhange_app)

# Currency Exchange Application

LIVE APP: https://currency-xchangeapp.herokuapp.com/

This is a simple Django app that integrates with [OpenExchangeRates](https://openexchangerates.org) to facilitate currency conversion and trasnfer of funds from wallet to wallet.

## **Supported Functions**
## Admins:
 URL: https://currency-xchangeapp.herokuapp.com/admin
- Initial Creation of Wallets after user has registered
- Overall access to all Models via Django admin

## Users
-  User Signup/Login (only requires username/password)
-  User able to set/update default currency and profile pic for each wallet
-  User can transfer cash to other registered users in any OpenExchangeRates supported currency from UI

## Setup Instructions
### Dependencies
This application has been developed and tested with the following technologies
1. Python 3.9.5
2. Django 3.2
3. Postgresql 12
4. Redis - used as Celery Broker
5. Pipenv

### Setting up Locally

1. Ensure all the listed dependencies are installed
2. Clone this repository
    ```bash
    $ git clone git@github.com:thoth-ky/currency_exhange_app.git
3. Create a database on Postgresql called `currency_exchange_app`, if a different name is used then ensure to provide it in .env
4. Acquire a `OPEN_EXCHANGE_RATES_APP_ID` from [OpenExchangeRates](https://openexchangerates.org)
5. Create a .env file from .env.example file provided and replace each value with the correct value
6. Run the following commands to setup the pipenv environemnt
    ```bash
    $ python -m pipenv shell
    $ pipenv install
    ```
7. Run database migrations
    ```bash
    $ python manage.py migrate
    ```
8. Update exchange rates
    ```bash
    $ python manage.py update_rates
    ```
9. Start the Celery Beat and Workers, this runs automated updates at Midnight daily, the schedule is configured using a crontab in `currency_exchange_app/celery.py`
    ```bash
     $ supervisord -c supervisord.conf
     $ supervisorctl -c supervisord.conf start all
    ```
10. To confirm everything is setup correctly, run tests
    ```bash
    $ pytest
    ```
11. Create initial admin user
    ```bash
    $ python manage.py createsuperuser
    ```
12. Start the server and access it on `http://localhost:8000`
    ```bash
    $ python manage.py runserver
    ```


### Using the Site

1. Signup as a user
2. Login as an administrator on the admin site using credentials for superuser
3. Proceed to create wallets for created users with an initial balance
4. As a user from the wallets page, select a single wallet
5. Select to update wallet details or perform trasnfer of funds
6. Submit the necessary details using the forms
7. Transactions TO/FROM the page are recorded in the wallets page

## Authors
 - Joseph Mutuku Kyalo
