![Epic Events logo](https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png)


# Epic Events

_API CRM destined to manage the activity of Epic Events (Clients, Contracts, Events)_

# Installation

### Epic Events uses posrgresql

You will need to install postgresql first:
```
$ sudo apt install postgresql
```

Then launch the posgres console with root rights:

```
$ sudo -u postgres psql
```

And then create a new database and a user.
Off course you can choose whatever names you whant, as long as it matches
your settings in django.
Lest's do that quickly here:

```sql
CREATE DATABASE epic_events;
CREATE USER epic_events_db_user_name WITH ENCRYPTED PASSWORD 'ZePassWeird';
ALTER ROLE epic_events_db_user_name SET client_encoding TO 'utf8';
ALTER ROLE epic_events_db_user_name SET default_transaction_isolation TO 'read committed';
ALTER ROLE epic_events_db_user_name SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE epic_events TO epic_events_db_user_name;
\q
```


### Download or clone the project files
(from github)

### Virtual environment

Create the virtual environment. In console:
```
$ python3 -m venv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```

Install the dependencies:

```
$ pip install -r requirements.txt
```

# Run the Application

### Apply the migrations
```
$ ./manage.py migrate
```

### Initialize the work groups (sale, support, managment)

```
$ ./manage.py shell < groups_initialize.py
```

### Run the server
```
$ ./manage.py runserver
```