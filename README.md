optional-django
===============

[![Build Status](https://travis-ci.org/markfinger/optional-django.svg?branch=master)](https://travis-ci.org/markfinger/optional-django)

Utils for providing optional support for django.

In short, this is a grab bag of utils to shim around environments which may or may not
include a configured version of django.


Installation
------------

```
pip install optional-django
```


Finding staticfiles
-------------------

```python
from optional_django.staticfiles import find

# Will resolve to an absolute path, if Django is configured and can find the file.
# Otherwise, None is returned
find('relative/path/to/file.txt')

# Will return the path provided, if it exists.
# Otherwise, None is returned
find('/absolute/path/to/file.txt')
```


six
---

```python
from optional_django import six

# optional_django has vendored a version of `six` to remove
# a dependency on `django.utils.six`
```


env
---

```python
# A boolean indicating if a module `django` can be found on the PYTHONPATH
# and it appears to resemble django's API
from optional_django.env import DJANGO_INSTALLED

# A boolean indicating that django appears to be configured
from optional_django.env import DJANGO_CONFIGURED

# if DJANGO_CONFIGURED is True, DJANGO_SETTINGS is django.conf.settings
# else, None
from optional_django.env import DJANGO_SETTINGS
```


serializers
-----------

```python
# if DJANGO_CONFIGURED is True, JSONEncoder is django.core.serializers.json.DjangoJSONEncoder
# else, JSONEncoder is json.JSONEncoder
from optional_django.serializers import JSONEncoder
```


Settings
--------

A basic configuration object which locks after it has been configured.

```python
from optional_django import conf

class Conf(conf.Conf):
    FOO = 'BAR'
    BAR = [1,2,3]
	WOZ = 4

settings = Conf()

print(settings.WOZ)  # 4, or the value of django.conf.settings.SOME_APP['WOZ']

# Raises an error
settings.WOZ = 5

# Use `configure` instead
settings.configure(
    FOO='some value',
    WOZ=5
)

print(settings.FOO)  # 'some value'
print(settings.BAR)  # [1, 2, 3]
print(settings.WOZ)  # 5

# Configure can only be called once, this raises an error
settings.configure(WOZ=10)
```


Running the tests
-----------------

```bash
mkvirtualenv optional-django
pip install -r requirements.txt
./runtests.sh
```
