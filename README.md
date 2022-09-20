# Dannes Django App

### About the application
This repo is a portfolio application made in Django. Its work in progress and will be updated as I learn more about 
Django. Hope you like it!

### How to get up and running with the application

### Create a virtual environment for the project
For every python project you need a virtual environment to install dependencies and 
enable execution of python scripts. Basic setup for it goes something like this:  
```
python virtualenv <env_name>
```
The version used while creating the project was `python v3.9.2` but any `v3.9.*` 
should do just fine.

### Activate the virtual environment
You need to activate the virtual environment and install the project 
dependencies in it before running the application is possible.  
Activate the virtual environment by running the following command:  
```
source ./<path_to_project_virtualenv>/bin/activate
```

### Install the dependencies
Since you now have a new virtual environment, activated it and you now need to install the project dependencies.
You can checkout whats specified in the `requirements.txt` file.  
To install all the dependencies form the specification run:  
```
pip install -r requirements.txt
```

### Database
You need to add a database somehow to run this application. Eather you use you own MariaDB/MySQL database and set it 
upp from the .env-example-file or you can just as easily use the sqlite3-database in the settings.py-file. One easy 
way to do this fast is to just comment out the database settings for MariaDB and change the name of the 
sqlite3-database settings to `default`. Make sure to create a sqlite3-database file named `db.sqlite3` in the project 
root folder. Now you need to make django aware of the changes you made in the settings.py-file by making the migrations.  
To do this you run the command:  
```
python manage.py makemigrations
```  
Followed by this command to create the tables in your new database:
```
python manage.py migrate
```

### Social Authentication setup
For the social authentication to work, you need to create a new application in the social media platform you want to 
use. There is an example of a key and a secret passed to a GitHub application. You may use GitHub as well or your 
perfect social authentication platform allowing you to do so. Please read up on the package 
[social-auth-app-django](https://pypi.org/project/social-auth-app-django/) documentation how to setup with your 
social media platform of choice.

### Start the application
Django starts the application by default on port `8000`.
To start the application run the command.
```
python manage.py runserver
```  

If you for any reason want to change the port, you can do so by passing the port number as an argument to the command.  
```
python manage.py runserver <port_number>
```  
Once everything is setup and running you should be able to access the application in your perfered browser at this URL.  
```
http://localhost:8000/
```  





```
Hope you like it!

Danne
```
