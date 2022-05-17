from django.contrib.auth.models import Group

"""Use this script with:
$ ./manage.py shell < groups_initialize.py

to create the groups, do it only once in a new database.
"""

group_sale = Group(name="sale")
group_sale.save()

group_support = Group(name="support")
group_support.save()
