from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

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
        fields = '__all__'


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
    contacts = ContactsSerializer(read_only=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')


class NetworkSupplierSerializer(ModelSerializer):
    """
    Сериализатор для получения поставщика
    """
    contacts = ContactsSerializer()
    products_count = SerializerMethodField()

    def get_products_count(self, obj):
        return obj.products.count()

    class Meta:
        model = NetworkNode
        exclude = ('debt', 'created_at', 'supplier', 'products')


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


class AddProductToNetworkNodeSerializer(ModelSerializer):
    """
    Сериализатор для добавления продукта к узлу сети
    """
    add_product = PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    added_product = SerializerMethodField()

    def get_added_product(self, obj):
        data = obj.products.last()
        return ProductSerializer(data).data

    class Meta:
        model = NetworkNode
        fields = ('add_product', 'added_product')

    def update(self, instance, validated_data):
        product = validated_data.pop('add_product')
        if instance.products.filter(id=product.id).exists():
            raise ValidationError('Продукт уже добавлен к данному узлу')
        if instance.level == 0:
            instance.products.add(product)
        else:
            check = instance.supplier.products.filter(id=product.id).exists()
            if check:
                instance.products.add(product)
            else:
                raise ValidationError('Продукт не найден у поставщика')
        return instance
