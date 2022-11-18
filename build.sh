#!/bin/sh
#chmod 755

# pull latest source
git pull origin master

# build django project
source ./venv/bin/activate
pip install -r ./requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# build vue app
cd app
yarn build

# use password supplied by github agent
echo $1 | sudo -S systemctlrestart gunicorn
echo $1 | sudo -S systemctlrestart nginx