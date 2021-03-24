# Formulář

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/PaulRoss1/Formular.git
$ cd Formular
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -3 -m venv env
$ env\Scripts\activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

Admin login:<br>
Username: admin<br>
Password: adminheslo

## Libraries used

ares-util==0.2.1<br/>
asgiref==3.3.1<br/>
certifi==2020.12.5<br/>
chardet==4.0.0<br/>
Django==3.1.7<br/>
idna==2.10<br/>
pytz==2021.1<br/>
requests==2.25.1<br/>
sqlparse==0.4.1<br/>
urllib3==1.26.4<br/>
xmltodict==0.12.0

## Python version
Python 3.8.1
