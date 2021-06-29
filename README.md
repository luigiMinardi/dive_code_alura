# dive_code_alura
Web API for image uploads made with python and django.

For start to use this API generate one Django Secret Key [here](https://djecrety.ir/) and paste in ``setup/settings.py`` in the ``SECRET_KEY = 'YourSecretKey'`` 
(and you will have something like ``SECRET_KEY = 'n-j8*!oe7!g&v_oi6b8-n_#si&-lyo=xhzb6sjtc8m8^7-qov@'``)3

## For use this repository you need the Python 3.7 (CPython*) or further

[Download Python Here](https://www.python.org/downloads/)

### create your virtual ambient
``python -m venv ./venv`` 

### activate your 'venv'
``source/venv/bin/activate`` (mac/linux)

``virtualenv\NAMEOFYOURVIRTUALENV\Scripts\activate`` (windows)

### Update your pip
``pip install --upgrade pip``
  
### install the dependecies
``pip install -r requirements.txt``

### Run the DataBase Migration
``python manage.py migrate``

### Create a Super User
``python manage.py createsuperuser``

### run server
``python manage.py runserver``


_If you have any trouble, feel free to open an issue._

*_If you don't know what is CPython, just use the python from python.org_

<!--Thanks to @cesardmn for improve the README.md-->
<!--https://github.com/cesardmn/dive_coding_alura-->
