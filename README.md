# Baby Track

As parents need to track a new baby's inputs and outputs very closely, the hospital or doctor will give them a printed spreadsheet to write down the vitals after every feeding or evolution.  This introduces the usual human problems of:
- Forgetting to log the event
- Losing the paper copies
- Logging wrong date or time
- Different date/time formats between parents
- Running out of forms 

Baby Track allows for either parent to enter the data from his/her phone, view the data without having to remember to bring paper copies and track multiple children in one interface

## Install
The project is setup as a standard Django project so any general Django deployment topology should work.  Given the amount of data, I've opted for the default SQLite database but all supported Django relational databases should work.  My current personal deployment is within a small local Debian VM that has Nginx serving the frontend/media/static with Gunicorn running the WSGI backend and SQLite3 as the database.  We access it either locally or over a VPN due to the lack of logon security currently in place.  For deployment step-by-step, the Digital Ocean guide is still the best in my opinion

<https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04>

***Note:*** "settings.py" is looking at environment variable "SECRET_KEY".  You can choose how to add this but I use the following to generate a new file with the key and add to the environment variables on boot.
`
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
`

## Roadmap
- [ ] Import/Export Feature (*currently using Pandas and CSV for mass data changes*)
- [ ] Native authentication (*this could currently be done via a reverse proxy/gateway with external auth source*)
- [ ] Increased tracking fields for age, height, weight
- [ ] Data graphing to view trends over time and compared to standard growth charts
- [ ] Cleaner frontend (*React frontend being worked*)
