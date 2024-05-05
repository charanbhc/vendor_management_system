from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Vendor models.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Purchase Order models.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_create(self, serializer):
        """
        Custom behavior when creating a Purchase Order.
        This method saves the order and can be used to update vendor performance metrics.
        """
        # Save the purchase order and update vendor metrics
        serializer.save()


class VendorPerformanceView(views.APIView):
    """
    APIView to calculate and retrieve performance metrics for a specific vendor.
    """
    def get(self, request, vendor_id):
        # Fetch vendor by ID
        vendor = get_object_or_404(Vendor, id=vendor_id)
        
        # Get all completed purchase orders for the vendor
        purchase_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

        # Calculate total number of completed purchase orders
        total_orders = purchase_orders.count()

        # Calculate on-time delivery rate
        on_time_deliveries = purchase_orders.filter(delivery_date__lte=po.order_date).count()
        on_time_delivery_rate = (on_time_deliveries / total_orders) * 100 if total_orders > 0 else 0

        # Calculate quality rating average
        quality_ratings = purchase_orders.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0

        # Calculate average response time
        acknowledgment_times = [
            (po.acknowledgment_date - po.issue_date).total_seconds()
            for po in purchase_orders.exclude(acknowledgment_date__isnull=True)
        ]
        average_response_time = (sum(acknowledgment_times) / len(acknowledgment_times)) if acknowledgment_times else 0

        # Calculate fulfillment rate (already calculated with on-time delivery rate)
        fulfillment_rate = on_time_delivery_rate

        # Prepare and return the response data
        performance_metrics = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        }

        return Response(performance_metrics, status=status.HTTP_200_OK)
