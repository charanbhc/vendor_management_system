from django.test import TestCase
from django.utils import timezone
from vendor_app.models import Vendor, PurchaseOrder


class VendorViewTestCase(TestCase):
    def setUp(self):
        # Create a vendor instance
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Test Contact Details",
            address="Test Address",
            vendor_code="V1234",
            on_time_delivery_rate=0.9,
            quality_rating_avg=4.5,
            average_response_time=2.5,
            fulfillment_rate=0.8,
        )

        # Provide an order_date using timezone.now()
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO123",
            vendor=self.vendor,
            order_date=timezone.now(),  # Set order_date to current time
            delivery_date=timezone.now() + timezone.timedelta(days=10),
            items={"item1": "Product1", "item2": "Product2"},
            quantity=100,
            status="pending",
            quality_rating=4.0,
            issue_date=timezone.now(),
        )

    # Add your test methods for view testing
