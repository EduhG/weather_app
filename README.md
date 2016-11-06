# Weather App
A weather application that displays graphs of temperatures based on time.

## How do I run this project locally?

The app is bundled with a database which contains some data. To run the app with the default username and password check it out [here](https://temp-grapher.herokuapp.com/).
#
    Username: edwin
    Password: admin2016

### 1. Clone the repository:

    git clone https://github.com/EduhG/weather_app.git

### 2. Create a virtual environment:

    virtualenv venv

### 3. Install project requirements:

    pip freeze -r requirements.txt

### 4. Navigate to project root directory:

    cd weather_app

#### To run the app:

    python manage.py runserver

### To see it in action, visit //127.0.0.1:8000/ in your web browser with the above login details

### 5. To do a fresh install delete the databse and recreate migrations:

    rm db.sqlite3
    python manage.py migrate --noinput

### 5. Run migrations:

    python manage.py migrate

### 6. Create a user:

    python manage.py createsuperuser

### 7. Run the server:

    python manage.py runserver

### 8. And open 127.0.0.1:8000/ in your web browser.
