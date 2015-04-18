optional-django
===============

[![Build Status](https://travis-ci.org/markfinger/optional-django.svg?branch=master)](https://travis-ci.org/markfinger/optional-django)

Utils for apps to provide optional support for django applications.

In short, this is a grab bag of utils to shim around environments which may or may not
include a configured version of django.


Installation
------------

```
pip install optional-django
```


Settings
--------

```python
from optional_django import conf

class Conf(conf.Conf):
    django_namespace = 'SOME_APP'

    FOO = 'BAR'
    BAR = [1,2,3]
	WOZ = 4

settings = Conf()

print(settings.WOZ)  # 4, or the value of django.conf.settings.SOME_APP['WOZ']

# If django is available and configured, Conf inspects django.conf.settings and
# looks for a dictionary named 'SOME_APP'. If found, it will override the defaults
# with any keys that match the Conf instance's attributes

# If django is not available or the namepace defined does not have a matching
# definition in settings, the user can override the defaults by calling `configure`
# on the Conf instance...

from some_app.conf import settings

settings.configure(
    FOO='some value',
    WOZ=5
)

print(settings.WOZ)  # 5
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


Running the tests
-----------------

```bash
mkvirtualenv optional-django
pip install -r requirements.txt
./runtests.sh
```
