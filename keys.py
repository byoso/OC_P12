"""Normally, this keys.py should not be shared online,
but Epic Events is a pedagogic project, so this file is then provided.

This file is expected to be uploaded through ssh connexion to the
production server.

It contains the secrets keys, and some settings that one could whant
to modify once the application is already deployed in production.
"""


# Debug
DEBUG = True
DATABASE_DEBUG = False  # True for sqlite, False for PostgreSQL
# set a prefix to 'hide' the site on production while operating with the
# test database.
DEBUG_DB_PREFIX = ""

# Secret settings
SECRET_KEY = 'django-insecure-o*o+=47zun+2o=q(t*lp++818bef%7*ok^ivkb2!q!144=_u3s'

# PostgreSQL DATABASE
DB_USER = 'epic_events_db_user_name'
DB_PASSWORD = 'ZePassWeird'
