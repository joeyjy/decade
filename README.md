# Decade

Require Python3.x, Django2.0

## Installation

1. Install python3
  
2. Install and make virtualenv

    $ pip install virtualenvwrapper  
    $ source /usr/local/bin/virtualenvwrapper.sh  
    $ mkvirtualenv -p python3 ENV_NAME  
    $ workon ENV_NAME  

3. Clone this repo

4. Install dependence

    $ cd decade  
    $ pip install -r requirements.txt  

5. Change database setting to your dev env

    $ cp decade/settings/dev.example decade/settings/dev.py  
    $ emacs decade/settings/dev.py  
    \# change DATABASES section  

6. create database (only fresh installation)

    $ python manage.py makemigrations

7. Launch

    $ python manage.py migrate  
    $ python manage.py runserver 0.0.0.0:8000  



 
