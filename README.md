# Restaurant-Kitchen-Service

This is a Django project created for interaction between the restaurant administrator, chefs.
The administrator is given the maximum rights to create new users and perform operations with dish and dish type.
Also, only users who are staff can create, update and delete dishes and types of dishes

# Guideline how to implement solution for Python tasks

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

Demo
View SuperUser:
![Website Interface](demo.png)
