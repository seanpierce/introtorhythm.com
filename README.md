# introtorhythm.com with Django and VUE (rebuild)

![Travis CI build badge](https://api.travis-ci.com/seanpierce/introtorhythm.com-rebuild.svg?branch=master) ![Test coverage badge](coverage.svg)

The purpose of this project it to take what I've learned with the [initial django build for introtorhythm.com](https://github.com/seanpierce/introtorhythm.com), and rebuild it to be cleaner and scalable.

**Specific goals:**

* Unit tesable (ongoing) ✓
  * Add coverage badge to README ✓
* CI/CD pipeline (in progress with Travis CI)
* Integration with VueJS ✓
* Exposed (and enhanced) _Subscriber_ and _Episodes_ API

## Installation

```shell
git clone [this repo] introtorhythm.com
python -m venv introtorhythm.com/
```

## Versions

* Django 2.2.4
* Python 3.6.3

## Usage

```shell
# navigate into the project root
# cd introtorhythm.com

# activate the virtual environment
source ./venv/bin/activate # mac
source ./venv/Scripts/activate # windows

# install dependencies
pip install -r requirements.txt

# migrate the database tables
python manage.py migrate

# run unit tests
python scripts/run-tests.py

# install front end dependencies
python scripts/install-frontend.py

# build the FE for development
python scripts/serve-frontend.py

# build the FE for production
python scripts/build-frontend.py

# start the development server
python manage.py runserver

```

## Resource list

* https://medium.com/@rodrigosmaniotto/integrating-django-and-vuejs-with-vue-cli-3-and-webpack-loader-145c3b98501a
