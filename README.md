# django-datetime-helpers

[![Build Status](https://travis-ci.org/eugen1j/django-datetime-helpers.svg?branch=master)](https://travis-ci.org/eugen1j/django-datetime-helpers)
[![codecov](https://codecov.io/gh/eugen1j/django-datetime-helpers/branch/master/graph/badge.svg?token=AE62KEYZHD)](https://codecov.io/gh/eugen1j/django-datetime-helpers)
[![PyPI version](https://badge.fury.io/py/django-datetime-helpers.svg)](https://badge.fury.io/py/django-datetime-helpers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/eugen1j/django-datetime-helpers/blob/master/LICENSE)


Frequently used functions and constants about datetime in Django projects


## Installing

    pip install django-datetime-helpers

## Examples
    

    # Quering all Users who join today
    users = User.objects.filter(
        created_at__date=today()
    )
    
    # Quering all Users who join in last 12 hours
    users = User.objects.filter(
        created_at__gte=secons_ago(12 * HOUR)
    )

    # Declaring constanst
    USER_SOMETHING_TIMEOUT = 5 * MINUTE
    
    # Waiting for something
    time.sleep(MINUTE)
    
For more examples see [source code](https://github.com/eugen1j/django-datetime-helpers/blob/master/django_datetime_helpers/helpers.py).