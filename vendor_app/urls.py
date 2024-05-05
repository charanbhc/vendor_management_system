from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'vendors', views.VendorViewSet)
router.register(r'purchase-orders', views.PurchaseOrderViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the router's URLs
    path('', include(router.urls)),
    
    # URL pattern for the VendorPerformanceView
    path('vendor-performance/<int:vendor_id>/', views.VendorPerformanceView.as_view(), name='vendor_performance'),
]
