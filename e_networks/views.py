from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from e_networks.models import NetworkNode
from e_networks.serializers import NetworkNodeCreateSerializer


class NetworkNodeCreateAPIView(CreateAPIView):
    """
    Создание узла сети
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeCreateSerializer
    permission_classes = [IsAuthenticated]
