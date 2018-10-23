# NOTICE !!!


* On initial clone/usage, when using MySql as database create a database with the current database name
found on the settings.py file (current database name on settings = 'musicstoredb')


* When using postgresql as database, uncomment the database configuration for postgresql and comment out
the database configuration for MySql on settings.py


* When trying to use the admin, create a superuser account for you to use (should be done once).
do so by :
  > python manage.py createsuperuser

don't forget the credentials.
