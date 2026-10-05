# Restaurant Menu (Django)

A restaurant menu site built with Django class-based views (`ListView`, `DetailView`). Dishes are grouped by course (starters, salads, mains, desserts), and unavailable dishes are shown struck through. Staff manage the menu through the Django admin.

`qr.py` generates a QR code that links to the menu.

## Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # add dishes at /admin
python manage.py runserver
```
