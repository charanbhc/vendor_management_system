from django.test import TestCase
from django.utils import timezone
from vendor_app.models import Vendor, PurchaseOrder

class PurchaseOrderTestCase(TestCase):
    def setUp(self):
        # Create a vendor instance for use in the tests
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="test@example.com",
            address="123 Test St",
            vendor_code="V123"
        )

    def test_purchase_order_creation(self):
        # Create a purchase order instance
        purchase_order = PurchaseOrder.objects.create(
            po_number="PO12345",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items='{"item1": {"name": "Item 1", "quantity": 10}}',
            quantity=10,
            status='pending',
            quality_rating=None,
            issue_date=timezone.now(),
            acknowledgment_date=None
        )

        # Assertions to test the purchase order was created correctly
        self.assertIsNotNone(purchase_order)
        self.assertEqual(purchase_order.po_number, "PO12345")
        self.assertEqual(purchase_order.vendor, self.vendor)
        self.assertEqual(purchase_order.quantity, 10)
        self.assertEqual(purchase_order.status, 'pending')
        self.assertIsNone(purchase_order.acknowledgment_date)

    def test_vendor_relationship(self):
        # Create a purchase order instance
        purchase_order = PurchaseOrder.objects.create(
            po_number="PO12346",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items='{"item2": {"name": "Item 2", "quantity": 5}}',
            quantity=5,
            status='completed',
            quality_rating=4.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now()
        )

        # Assertions to test the vendor relationship
        self.assertEqual(purchase_order.vendor, self.vendor)
        self.assertIn(purchase_order, self.vendor.purchase_orders.all())
