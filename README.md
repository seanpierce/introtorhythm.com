# introtorhythm.com

![Travis CI build badge](https://api.travis-ci.com/seanpierce/introtorhythm.com.svg?branch=master) ![Test coverage badge](coverage.svg)

Intro To Rhythm is a freeform mix series and live-streaming audio station that began in 2017. All episodes and content are owned by their creators and made exclusively for Intro To Rhythm.

Additionally, ITR is dedicated to open-source projects, and the collective idea sharing that fuels creative expression. If you're interested in developing your own live-streaming station or podcasting platform, you're invited to refer to ITR's source code (Licence MIT).

Send questions and comments to introtorhythm@gmail.com

-----

The purpose of this project it to take what I've learned with the [initial django build for introtorhythm.com](https://github.com/seanpierce/introtorhythm.com-archive), and rebuild it to be cleaner and scalable.

**Specific goals:**

* Unit tesable (ongoing) ✓
  * Add coverage badge to README ✓
* CI/CD pipeline (in progress with Travis CI)
* Integration with VueJS ✓
  * Using Vue Router and Vuex ✓
* Exposed (and enhanced) _Subscriber_ and _Episodes_ API ✓
* Repository design pattern ✓

## Dependencies

* Node v12 or greater
* Python v3.8 or greater
* Python's `virtualenv` package v20 or greater


## Project Versions

* Django 3.1.4
* Python 3.8.10


## Installation

```shell
# download repo
git clone [this repo] introtorhythm.com

# if virtualenv is already installed, set up virtual environment
python -m venv introtorhythm.com/

# else, install virtualenv, then run the previous step
pip install virtualenv

# install project packages
cd introtorhythm.com
pip install -r requirements.txt

# install the front-end app
cd app
yarn [or npm] install
```

Note - the `introtorhythm.com/settings.py` file requires certain config values to be set in a file called `env.ini` in the project root. If you're running this for the first time, you can copy the values from the `example.env.ini` file also found in the project root. Ensure that the `env.ini` file does not go to source control. Similarly, ensure that that any _real_ env keys do not get committed to the `example.env.ini` file.


## Usage

```shell
# navigate into the project root
# cd introtorhythm.com

# activate the virtual environment
source ./venv/bin/activate # mac/ linux
source ./venv/Scripts/activate # windows

# migrate the database tables
python manage.py migrate

# run unit tests
python scripts/run-tests.py

# start the back-end server
python manage.py runserver

# build front-end application
cd app
yarn serve
```

# More info

For more information regarding [configuration](https://github.com/seanpierce/introtorhythm.com/wiki/Configuration) and [cron jobs](https://github.com/seanpierce/introtorhythm.com/wiki/Cron-Jobs), check [the wiki](https://github.com/seanpierce/introtorhythm.com/wiki)!
