optional-django
===============

[![Build Status](https://travis-ci.org/markfinger/optional-django.svg?branch=master)](https://travis-ci.org/markfinger/optional-django)

Utils for apps to provide optional support for django applications. In short,
this is a grab bag of utils to shim around environments which may or may not
include a configured version of django.


Installation
------------

`pip install optional-django`


Settings
--------

```python
from optional_django.conf import Conf

settings = Conf('SOME_APP', {
	# defaults
	'FOO': 'BAR',
	'ONE': 1,
})

settings.FOO  # 'BAR', or an overridden value

# If django is available and configured, Conf inspects django.conf.settings and
# updates the defaults, if it finds a dictionary named 'SOME_APP'.

# If django is not available, the user can override your `settings` by importing
# the variable and calling `settings.configure({ 'FOO': 'WOO' })`, which will
# update your defaults.
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


Running the tests
-----------------

```bash
mkvirtualenv optional-django
pip install -r requirements.txt
./runtests.sh
```
