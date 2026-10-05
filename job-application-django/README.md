# Job Application Form (Django)

The [Flask job form](../job-application-flask) rebuilt in Django:

- Django `Form` validation and a `Form` model
- template inheritance (`base.html`) with a navbar and an About page
- a customised admin panel (list display, search, filters, ordering) to review applications

## Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # to use /admin
python manage.py runserver
```
