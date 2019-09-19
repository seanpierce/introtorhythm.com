# introtorhythm.com

![Travis CI build badge](https://api.travis-ci.com/seanpierce/introtorhythm.com-rebuild.svg?branch=master) ![Test coverage badge](coverage.svg)

Intro To Rhythm is a freeform mix series and live-streaming audio station that began in 2017. All episodes and content are owned by their creators and made exclusively for Intro To Rhythm.

Additionally, ITR is dedicated to open-source projects, and the collective idea sharing that fuels creative expression. If you're interested in developing your own live-streaming station or podcasting platform, you're invited to refer to ITR's source code (Licence MIT).

Send questions and comments to introtorhythm@gmail.com

-----

The purpose of this project it to take what I've learned with the [initial django build for introtorhythm.com](https://github.com/seanpierce/introtorhythm.com), and rebuild it to be cleaner and scalable.

**Specific goals:**

* Unit tesable (ongoing) ✓
  * Add coverage badge to README ✓
* CI/CD pipeline (in progress with Travis CI)
* Integration with VueJS ✓
* Exposed (and enhanced) _Subscriber_ and _Episodes_ API

## Views

### Desktop Views
| Main | Details |
|:-----|:--------|
|![](https://user-images.githubusercontent.com/15679739/64751042-c3cfb900-d4cf-11e9-9ab6-ee37f24562ce.png)|![](https://user-images.githubusercontent.com/15679739/64751177-3fca0100-d4d0-11e9-80a6-787d19f3de0e.png)|

### Mobile Views
| Main | Mobile Nav | Details |
|:-----|:-----------|:--------|
|![](https://user-images.githubusercontent.com/15679739/64751043-c3cfb900-d4cf-11e9-9279-09f8b6af3f20.png)|![](https://user-images.githubusercontent.com/15679739/64751044-c3cfb900-d4cf-11e9-8d77-f1bec2260b86.png)|![](https://user-images.githubusercontent.com/15679739/64751554-5c1a6d80-d4d1-11e9-95f1-076312d56236.png)|

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

# start the development server
python manage.py runserver

```

## Resource list

* https://medium.com/@rodrigosmaniotto/integrating-django-and-vuejs-with-vue-cli-3-and-webpack-loader-145c3b98501a
