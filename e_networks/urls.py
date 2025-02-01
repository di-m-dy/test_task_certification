from django.urls import path
from e_networks.apps import ENetworksConfig
from e_networks.views import NetworkNodeCreateAPIView, NetworkNodeRetrieveAPIView, NetworkNodeListAPIView, \
    NetworkNodeUpdateAPIView, NetworkNodeDestroyAPIView, AddProductUpdateAPIView, ProductViewSet, ContactsViewSet

from rest_framework.routers import DefaultRouter

app_name = ENetworksConfig.name

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename='products')
router.register(r"contacts", ContactsViewSet, basename='contacts')

urlpatterns = [
                  path('create/', NetworkNodeCreateAPIView.as_view(), name='network-node-create'),
                  path('<int:pk>/', NetworkNodeRetrieveAPIView.as_view(), name='network-node-detail'),
                  path('<int:pk>/update/', NetworkNodeUpdateAPIView.as_view(), name='network-node-update'),
                  path('<int:pk>/delete/', NetworkNodeDestroyAPIView.as_view(), name='network-node-delete'),
                  path('', NetworkNodeListAPIView.as_view(), name='network-node-list'),
                  path('<int:pk>/add_product/', AddProductUpdateAPIView.as_view(), name='add-product-to-network-node'),
              ] + router.urls
