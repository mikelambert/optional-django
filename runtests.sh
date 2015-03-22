echo "Running without_django tests"
nosetests -w tests/without_django/
echo
echo "Running with_django tests"
python tests/runtests_with_django.py