from django.contrib import admin
from .models import Invoice , InvoiceDetail
# Register your models here.

#Adding models to the admin site
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)