# Dannes Django App

### About the application
This repo is a portfolio application made in Django. Its work in progress and will be updated as I learn more about Django. Hope you like it!

### How to get up and running with the application

#### Create a virtual environment for the project
For every python project you need a virtual environment to execute scripts. Basic setup for it goes something like this:  
```python virtualenv <env_name>```  
The version used while creating the project was `python v3.9.2` but any `v3.9.*` should do just fine.

##### Activate the virtual environment
You need to activate the virtual environment and install the project dependencies in it before running the application is possible. 
Activate the virtual environment by running the following command:  
```source ./<path_to_project_virtualenv>/bin/activate```

#### Install the dependencies
Since you now have a new virtual environment, you need to install the dependencies for the project. 
You can checkout the specification in the file `requirements.txt` before installing and install them with the command:  
```pip install -r requirements.txt```

##### Start the application
```python manage.py runserver```

Now you should be able to access the application at 
```http://localhost:8000/```  

Enjoy!


```
Daniel Andersson
```
