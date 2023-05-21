# DRF TEMPLATE

A template for launching new Django Rest Framework projects quickly.

## Features

- Django 4.2.1 & Rest 3.14.0
- django-environ for reading env files
- Documentation using drf-spectacular
- Custom User Model
- CORS headers
- Token Authentication
- Signup/login/logout/passwordreset with dj-rest-auth

## Setup

1. Clone repo  
    ```shell
    git clone https://github.com/khaled5321/DRF-Project-Template.git
    ```

2. Create virtual environment
    ```shell
    python -m venv venv
    ```

3. Install requirements
    ```shell
    pip install -r requirements.txt
    ```

4. Make migrations & migrate
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Provide password reset view

    Uncomment the url path in urls.py and provide a custom view.  

    ```python 
    path(
    "auth/password/reset/confirm/<uidb64>/<token>/",
    custom view,
    name="password_reset_confirm", # keep tha name
    )
    ```
    
    The view direct the user to the frontend to enter the new password.  
    Send a post request with the new password, uid and token to ```/api/v1/auth/password/reset/confirm/``` to confirm the password reset.

6. Provide verify Email view

    Uncomment the url path in urls.py and provide a custom view. 

    ```python 
    path(
    "api/v1/registration/account-confirm-email/<key>/",
    custom view,
    name="account_confirm_email" # keep the name
    )
    ```

    The view should direct the user to the frontend to inform him that his email was verified  
    Send a post request with the key to ```/api/v1/registration/verify-email/``` to verify the email