﻿# Restaurant-Kitchen-Service

This is a Django project created for interaction between the restaurant administrator, chefs.
The administrator is given the maximum rights to create new users and perform operations with dish and dish type.
Also, only users who are staff can create, update and delete dishes and types of dishes

# Features

1. Create new user(only for superuser)
2. Cheat what dish type and dish can prepare Cook's
3. Create, update and delete dish type (all staff)
4. Create, update and delete dish (all staff)

## Prepare the project

1. Fork the repo (GitHub repository)
2. Clone the forked repo
    ```
    git clone the-link-from-your-forked-repo
    ```
    - You can get the link by clicking the `Clone or download` button in your repo
3. Open the project folder in your IDE
4. Open a terminal in the project folder
5. Create a branch for the solution and switch on it
    ```
    git checkout -b develop
    ```
    - You can use any other name instead of `develop`
6. If you are using PyCharm - it may propose you to automatically create venv for your project
   and install requirements in it, but if not:
    ```
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
    ```
7. For using ready database:

   ```
   python manage.py migrate
   python manage.py loaddata restaurant.json
   ```

8. Run the development server:

   ```
   python manage.py runserver
   ```

9. Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.

10. Environment setup
    The project uses environment variables for configuration. For proper operation, you need to create a .env file that
    contains all the necessary variables.

In the root directory of your project, create a .env file and add the following environment variables to it:

   ```
   # Django secret key (change to your secret key)
   DJANGO_SECRET_KEY=your_secret_key_here
   
   # Debug mode (True or False)
   DEBUG=True
   
   # Database URL (e.g. PostgreSQL, MySQL, or SQLite)
   DATABASE_URL=your_database_url_here
   
  ```
   # Link
   https://restaurant-kitchen-service-1.onrender.com/
   AWS Link: http://51.20.121.175/accounts/login/?next=/dishs/

If you don't want to register you can log in with this credentials:

Login: SuperUser
Password: Skoda4752

Login: IsStaff
Password: Skoda4752

Login: NotStaff
Password: Skoda4752

  ```
# Demo
View SuperUser:
![Website Interface](demo.png)
