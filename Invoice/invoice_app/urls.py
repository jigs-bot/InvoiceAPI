from django.urls import path
from .views import (
    invoice_list,
    invoice_detail,
    invoice_detail_list,
    invoice_detail_view,
)

urlpatterns = [
    path('invoices/', invoice_list, name='invoice-list'),
    path('invoices/<int:pk>/', invoice_detail, name='invoice-detail'),
    
    path('invoice_details/', invoice_detail_list, name='invoice-detail-list'), 
    path('invoice_detail/<int:pk>/', invoice_detail_view, name='invoice-detail-view'),
]
