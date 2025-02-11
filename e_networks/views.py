from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters import rest_framework as filters

from e_networks.models import NetworkNode, Product, Contacts
from e_networks.paginators import CustomPaginator
from e_networks.serializers import NetworkNodeCreateSerializer, NetworkNodeRetrieveSerializer, \
    NetworkNodeListSerializer, NetworkNodeUpdateSerializer, ProductSerializer, AddProductToNetworkNodeSerializer, \
    ContactsSerializer


class NetworkNodeCreateAPIView(CreateAPIView):
    """
    Создание узла сети
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeCreateSerializer
    permission_classes = [IsAuthenticated]


class NetworkNodeUpdateAPIView(UpdateAPIView):
    """
    Обновление узла сети
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeUpdateSerializer
    permission_classes = [IsAuthenticated]


class NetworkNodeRetrieveAPIView(RetrieveAPIView):
    """
    Получение узла сети
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeRetrieveSerializer
    permission_classes = [IsAuthenticated]


class NetworkNodeListAPIView(ListAPIView):
    """
    Список узлов сети
    Фильтрация по стране: ?contacts__country=RU
    Узнать код страны можно по ссылке: https://www.iso.org/obp/ui#search
    """
    queryset = NetworkNode.objects.all().order_by('-created_at')
    serializer_class = NetworkNodeListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contacts__country',)


class NetworkNodeDestroyAPIView(DestroyAPIView):
    """
    Удаление узла сети
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeRetrieveSerializer
    permission_classes = [IsAuthenticated]


class AddProductUpdateAPIView(UpdateAPIView):
    """
    Обновление продукта
    """
    queryset = NetworkNode.objects.all()
    serializer_class = AddProductToNetworkNodeSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    """
    Вьюсет для продуктов
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPaginator
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'model', 'release_date')

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [IsAuthenticated()]
        return [IsAdminUser()]


class ContactsViewSet(ModelViewSet):
    """
    Вьюсет для контактов
    """
    queryset = Contacts.objects.all().order_by('id')
    serializer_class = ContactsSerializer
    pagination_class = CustomPaginator
    permission_classes = [IsAuthenticated]
