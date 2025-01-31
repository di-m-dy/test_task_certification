from rest_framework.serializers import ModelSerializer

from e_networks.models import NetworkNode, Contacts, Product


class ContactsSerializer(ModelSerializer):
    """
    Сериализатор для контактов
    """

    class Meta:
        model = Contacts
        fields = '__all__'


class NetworkNodeCreateSerializer(ModelSerializer):
    """
    Сериализатор для пользователя
    """

    contacts = ContactsSerializer()

    class Meta:
        model = NetworkNode
        fields = '__all__'

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        contacts = Contacts.objects.create(**contacts_data)
        network_node = NetworkNode.objects.create(contacts=contacts, **validated_data)
        return network_node

