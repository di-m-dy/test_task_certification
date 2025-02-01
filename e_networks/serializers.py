from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, BaseSerializer

from e_networks.models import NetworkNode, Contacts, Product


class ContactsSerializer(ModelSerializer):
    """
    Сериализатор для контактов
    """

    class Meta:
        model = Contacts
        exclude = ('id',)


class ProductSerializer(ModelSerializer):
    """
    Сериализатор для продуктов
    """

    class Meta:
        model = Product
        fields = ('name', 'model', 'release_date')



class NetworkNodeCreateSerializer(ModelSerializer):
    """
    Сериализатор для создания узла сети
    """

    contacts = ContactsSerializer()

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        contacts = Contacts.objects.create(**contacts_data)
        network_node = NetworkNode.objects.create(contacts=contacts, **validated_data)
        return network_node


class NetworkNodeUpdateSerializer(ModelSerializer):
    """
    Сериализатор для обновления узла сети
    """
    contacts = ContactsSerializer()

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')



class NetworkSupplierSerializer(ModelSerializer):
    """
    Сериализатор для получения поставщика
    """
    contacts = ContactsSerializer()

    class Meta:
        model = NetworkNode
        exclude = ('debt', 'created_at', 'supplier')



class NetworkNodeRetrieveSerializer(ModelSerializer):
    """
    Сериализатор для получения узла сети
    """
    contacts = ContactsSerializer()
    products = ProductSerializer(many=True)
    supplier = NetworkSupplierSerializer()

    class Meta:
        model = NetworkNode
        fields = '__all__'



class NetworkNodeListSerializer(ModelSerializer):
    """
    Сериализатор для списка узлов сети
    """
    # Количество продуктов у данного узла
    product_count = SerializerMethodField()
    def get_product_count(self, obj):
        return obj.products.count()
    # уровень иерархии узла
    level = SerializerMethodField()
    def get_level(self, obj):
        level = 0
        while obj.supplier:
            level += 1
            obj = obj.supplier
        return level

    contacts = ContactsSerializer()
    supplier = NetworkSupplierSerializer()

    class Meta:
        model = NetworkNode
        fields = ('id', 'name', 'contacts', 'supplier', 'debt', 'created_at', 'product_count', 'level')


class NetworkDestroySerializer(ModelSerializer):
    """
    Сериализатор для удаления узла сети
    """

    class Meta:
        model = NetworkNode
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')
