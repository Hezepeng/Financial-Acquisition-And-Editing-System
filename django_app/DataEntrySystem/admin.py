from django.contrib import admin

# Register your models here.
from DataEntrySystem.models import pdf_information, target_company_package, basic_plan_essential_information

admin.site.register(pdf_information)
admin.site.register(target_company_package)
admin.site.register(basic_plan_essential_information)
