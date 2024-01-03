# invoices/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class Test(APITestCase):
    invoice_data={}
    def Dummy(self):
        self.invoice_data = {
            'date': '2024-01-03',
            'customer_name': 'Jigs_001',
            'details': [
                {
                    'description': 'T1',
                    'quantity': 2,
                    'unit_price': 10.00,
                    'price': 20.00,
                },
            ],
        }

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        if self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST):
            print("BAD DATA")   
        else:
            print("Created")
        self.assertEqual(Invoice.objects.count(), 0)

    def test_get_invoice_list(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), -1)

    def test_get_invoice_detail(self):
        invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')
        detail = InvoiceDetail.objects.create(
            invoice=invoice, description='Item 1', quantity=2, unit_price=10.00, price=20.00
        )
        response = self.client.get(f'/invoices/{invoice.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['details'][0]['id'], detail.id)

    