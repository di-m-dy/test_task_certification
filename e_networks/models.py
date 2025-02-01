from django.db import models
from django_countries.fields import CountryField


class FactoryLicense(models.Model):
    """
    Модель лицензии на производство
    Без этой лицензии звено сети с нулевым статусом не может добавить продукт
    is_approved - поле, которое показывает, подтверждена ли лицензия (меняется администратором)
    """
    factory = models.OneToOneField(
        'NetworkNode',
        on_delete=models.CASCADE,
        verbose_name='Звено сети',
        related_name='license'
    )
    is_approved = models.BooleanField(verbose_name='Лицензия подтверждена', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"License#{self.pk}-{self.factory}"

    class Meta:
        verbose_name = 'лицензия на производство'
        verbose_name_plural = 'лицензии на производство'


class Contacts(models.Model):
    """
    Модель контактов
    """
    email = models.EmailField(verbose_name='Email', unique=True)
    country = CountryField(verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город', null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name='Улица', null=True, blank=True)
    house = models.IntegerField(verbose_name='Номер дома', null=True, blank=True)
    google_map_link = models.URLField(verbose_name='Ссылка на Google Maps', null=True, blank=True)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'



class NetworkNode(models.Model):
    """
    Модель звена сети по продаже товаров электроники
    """
    name = models.CharField(max_length=255, verbose_name='Наименование')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', null=True, blank=True)
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Долг перед поставщиком',
        null=True,
        blank=True,
        default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


class Product(models.Model):
    """
    Модель продукта
    """
    network_node = models.ForeignKey(
        NetworkNode,
        on_delete=models.CASCADE,
        verbose_name='Сетевое звено',
        related_name='products'
    )
    name = models.CharField(max_length=255, verbose_name='Наименование')
    model = models.CharField(max_length=255, verbose_name='Модель', null=True, blank=True)
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок', null=True, blank=True)
    count = models.IntegerField(verbose_name='Количество', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
