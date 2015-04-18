echo "Running tests/without_django"
nosetests -w tests/without_django/
echo
echo "Running tests/with_django"
python tests/runtests_with_django.py