# introtorhythm.com with Django and VUE (rebuild)

The purpose of this project it to take what I've learned with the initial django build for introtorhythm.com, and rebuild it to be cleaner and scalable.

**Specific goals:**

* Unit tesable
* CI/CD pipeline
* Integration with VueJS
* Exposed (and enhanced) _Subscriber_ and _Episodes_ API

## Installation

```shell
mkdir introtorhythm.com
python -m venv introtorhythm.com/
touch introtorhythm/settings.ini
git clone [this repo] introtorhythm.com/introtorhythm
```

The project structure should look like this:

```ini
introtorhythm.com/
    introtorhythm/
        [django project/ this repository]
    venv/
    settings.ini
```

## Versions

* Django 2.2.4
* Python 3.6.3

## Usage

```shell
# navigate into the project root
# cd introtorhythm.com

# activate the virtual environment
source ../venv/Scripts/activate

# install dependencies
pip install -r requirements.txt

# migrate the database tables
python manage.py migrate

# run unit tests
python manage.py test episode.tests

# start the development server
python manage.py runserver

# install front end dependencies
yarn i

# build the FE for development
yarn run watch

# build the FE for production
yarn run build
```

## Resource list

* [crud-app-using-vue-js-and-django](https://medium.com/quick-code/crud-app-using-vue-js-and-django-516edf4e4217)
* [django-vuejs-tutorial](https://github.com/michaelbukachi/django-vuejs-tutorial/wiki/Django-Vue.js-Integration-Tutorial)
* [clean-architecture-in-django](https://engineering.21buttons.com/clean-architecture-in-django-d326a4ab86a9)
