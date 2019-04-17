"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from DataEntrySystem import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/getKeyValueList', views.get_key_value_list),
  path('api/getFormData', views.get_form_data),
  path('api/getTableRowData', views.get_table_row_data),
  path('api/getTableData', views.get_table_data),
  path('api/saveSingleData', views.save_single_data),
  path('api/saveTableRowData', views.save_table_row_data),
  path('api/deleteTableRowData', views.delete_table_row_data),
  path('api/uploadPdf', views.upload_pdf),
  path('api/getPdf', views.get_pdf),
  path('api/getAllCompany', views.get_all_company),
  path('api/getAllCompanyPackage', views.get_all_company_package),
  path('api/saveCompanyPackage', views.save_company_package),
  path('api/deleteCompanyPackage', views.delete_company_package),
  path('api/deletePdf', views.delete_pdf)

]
