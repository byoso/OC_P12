from django.contrib.auth.models import Group, Permission

from tools import color

"""Use this script to create the groups in a new database,
do it only once :
$ ./manage.py shell < groups_initialize.py


"""

# Group Sale
group = Group.objects.filter(name="sale")
if not group.exists():
    group_sale = Group.objects.create(name="sale")
    permissions = [
        Permission.objects.get(codename="add_client"),
        Permission.objects.get(codename="change_client"),
        Permission.objects.get(codename="view_client"),
        Permission.objects.get(codename="add_contract"),
        Permission.objects.get(codename="change_contract"),
        Permission.objects.get(codename="view_contract"),
        Permission.objects.get(codename="add_event"),
    ]

    for permission in permissions:
        group_sale.permissions.add(permission)
    group_sale.save()
    print(
        f"{color['success']} Group 'sale' successfully created."
        f" {color['end']}"
        )
else:
    print("a 'sale' group already exists")


# Group Suppoport
group = Group.objects.filter(name="support")
if not group.exists():
    group_support = Group.objects.create(name="support")
    permissions = [
        Permission.objects.get(codename="view_client"),
        Permission.objects.get(codename="change_event"),
        Permission.objects.get(codename="view_event"),
    ]

    for permission in permissions:
        group_support.permissions.add(permission)
    group_support.save()
    print(
        f"{color['success']} Group 'support' successfully created."
        f" {color['end']}"
        )
else:
    print("a 'support' group already exists")
