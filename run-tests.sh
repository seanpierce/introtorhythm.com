# run tests with coverage
coverage run manage.py test

# generate coverage badge
rm coverage.svg || true
coverage-badge -o coverage.svg