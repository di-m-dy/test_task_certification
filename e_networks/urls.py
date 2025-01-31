from django.urls import path
from e_networks.apps import ENetworksConfig
from e_networks.views import NetworkNodeCreateAPIView

app_name = ENetworksConfig.name

urlpatterns = [
    path('create/', NetworkNodeCreateAPIView.as_view(), name='network-node-create'),
    ]

