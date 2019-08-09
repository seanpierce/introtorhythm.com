import os

# run tests with coverage
os.system('coverage run manage.py test')

# generate coverage badge

os.system('rm coverage.svg || true')
os.system('coverage-badge -o coverage.svg')