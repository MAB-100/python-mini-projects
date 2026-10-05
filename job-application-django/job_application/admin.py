from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "date", "occupation"]  # Display these fields in the admin site
    search_fields = ["first_name", "last_name", "email"]  # Add a search bar to the admin site
    list_filter = ["date", "occupation"]  # Add filters to the admin site
    ordering = ["-date"]  # Order the forms by date in descending order
    


admin.site.register(Form, FormAdmin)  # Register the Form model with the admin site

