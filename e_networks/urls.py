from django.urls import path
from e_networks.apps import ENetworksConfig
from e_networks.views import NetworkNodeCreateAPIView, NetworkNodeRetrieveAPIView, NetworkNodeListAPIView, \
    NetworkNodeUpdateAPIView, NetworkNodeDestroyAPIView

app_name = ENetworksConfig.name

urlpatterns = [
    path('create/', NetworkNodeCreateAPIView.as_view(), name='network-node-create'),
    path('<int:pk>/', NetworkNodeRetrieveAPIView.as_view(), name='network-node-detail'),
    path('<int:pk>/update/', NetworkNodeUpdateAPIView.as_view(), name='network-node-update'),
    path('<int:pk>/delete/', NetworkNodeDestroyAPIView.as_view(), name='network-node-delete'),
    path('', NetworkNodeListAPIView.as_view(), name='network-node-list'),
]

