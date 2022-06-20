### Steps: ###
    1. Clone this repo 
    2. Create a virtual env in the root folder using the following command  `python3 -m venv venv'. This will create a virtual environment call venv. If you decide to call it something else, please add the directory to the gitignore and virtual env folders should not be part of the repo.
    3. Once created activate the virtual environment using `source venv/bin/activate`.
        * export RDS_PORT=3306
        * export RDS_DB_NAME=<name>
        * export RDS_PASSWORD=
        * export RDS_USERNAME=
        * export RDS_HOSTNAME=localhost
        
    5. Run `pip install -r requirements.txt` to install all the required packages.
    6. Run `python manage.py migrate` to run all migrations
    7. Run `python manage.py createsu` to create the super user in the db with username admin and password admin.
    8. Run `python manage.py runserver` to run the server and access it on localhost:8000 in the browser
    