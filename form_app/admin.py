from django.contrib import admin
from form_app.models import Formular


class FormularAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Formular, FormularAdmin)
