from _typeshed import Self
from typing import ClassVar, Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.expressions import Value
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'




class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return super.__name__

class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(max_length=300, verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return super.title

class Notebook(Product):
    diagonal = models.CharField(max_length=150, verbose_name='Диагональ')
    display = models.CharField(max_length=150, verbose_name='Тип дисплея')
    processor_freg = models.CharField(max_length=200, verbose_name='Частота процессора')
    ram = models.CharField(max_length=250,verbose_name='Оперативная память')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class Smartfone(Product):
    diagonal = models.CharField(max_length=150, verbose_name='Диагональ')
    display_type = models.CharField(max_length=150, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=200, verbose_name='Разрешение экрана')
    accum_volume = models.CharField(max_length=250,verbose_name='Обьем батареи')
    sd = models.BooleanField(default=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class Clothes(Product):
    size = models.CharField(max_length=150, verbose_name='Размер')
    сolour = models.CharField(max_length=150, verbose_name='Цвет')
    brend = models.CharField(max_length=200, verbose_name='Бренд')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class Shoes(Product):
    size = models.CharField(max_length=150, verbose_name='Размер')
    сolour = models.CharField(max_length=150, verbose_name='Цвет')
    brend = models.CharField(max_length=200, verbose_name='Бренд')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class Cars(Product):
    model = models.CharField(max_length=150, verbose_name='Модель')
    сolour = models.CharField(max_length=150, verbose_name='Цвет')
    brend = models.CharField(max_length=200, verbose_name='Бренд')
    year_of_issue = models.CharField(max_length=200, verbose_name='Год выпуска')
    engine_power = models.CharField(max_length=200, verbose_name='Можность двигателя')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class immovables(Product):
    square = models.CharField(max_length=150, verbose_name='Площадь квартиры')
    rooms = models.CharField(max_length=150, verbose_name='Колличество комнат')
    area = models.CharField(max_length=200, verbose_name='Район размещения')
    not_completedsd = models.BooleanField(default=True)


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='releted_products')
    content_type = models.PositiveBigIntegerField(ContentType, on_delet=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая Цена' )

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)



class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='releted_cart')
    total_product = models.PositiveBigIntegerField(default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая Цена' )

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    address = models.CharField(max_length=300, verbose_name='Адрес')

    def __str__(self):
        return "Продукт: {} {}".format(self.user.first_name, self.user.last_name)


class Advert(models.Model):
    title = models.CharField("Название", max_length=150)
    text = models.TextField("Описание", max_length=700)
    author = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=user_avatar_path)
    likes = models.ManyToManyField(User, related_name='user_likes_it', blank=True)
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural ="Обьявления"

        

