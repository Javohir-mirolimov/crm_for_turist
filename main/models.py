from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    age = models.IntegerField(default=18, null=True, blank=True)
    state = models.CharField(max_length=55, null=True, blank=True)
    region = models.CharField(max_length=55, null=True, blank=True)
    addres_street = models.CharField(max_length=55, null=True, blank=True)
    sex = models.CharField(max_length=55, null=True, blank=True)
    nationality = models.CharField(max_length=55, null=True, blank=True)
    password_series = models.CharField(max_length=25, null=True, blank=True)
    status = models.IntegerField(default=5, choices=(
        (1, 'direktor'),
        (2, 'manager'),
        (3, 'admin'),
        (4, 'turist'),
        (5, 'other'),
    ))

    def __str__(self):
        return self.username


    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Sponsors(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
class Service(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Image(models.Model):
    img = models.ImageField(upload_to='img_hotel/')

class Hotel(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    category_address = models.ForeignKey(to='Sub_category_address', on_delete=models.PROTECT)
    reting = models.FloatField(default=0)
    sponsors = models.ManyToManyField(to='Sponsors', blank=True)
    service = models.ManyToManyField(to='Service')
    open_time = models.DateField()
    card = models.IntegerField()
    photo = models.ManyToManyField(to='Image')
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(selfs):
        return selfs.name


class Category_address(models.Model):
        name = models.CharField(max_length=55)
        craete_at = models.DateField(auto_now=True)

        def __str__(self):
            return self.name

class Sub_category_address(models.Model):
        name = models.CharField(max_length=55)
        category = models.ForeignKey(to='Category_address', on_delete=models.CASCADE)
        craete_at = models.DateField(auto_now=True)

        def __str__(self):
            return self.name

class Room_Image(models.Model):
    photo = models.ImageField(upload_to="hotel_room_img/")

class Room(models.Model):
    hotel_room = models.ForeignKey(to='Hotel',on_delete=models.CASCADE)
    name = models.CharField(max_length=35, unique=True)
    number_people = models.IntegerField()
    luks = models.BooleanField(default=False)
    lusk_room = models.IntegerField(default=4 ,choices=(
        (1, 'tv'),
        (2, 'frige'),
        (3, 'safe'),
        (4, 'microtalk'),
    ))
    free_porkofka = models.BooleanField(default=False)
    free_wifi = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    img = models.ManyToManyField(to='Room_Image')
    is_delivery = models.BooleanField(default=False)
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Order_room(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    order_room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    dadline = models.DateTimeField()
    create_at = models.DateField(auto_now=True)


class Achievement(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to="yutuq_img/")

class Hotel_food(models.Model):
    name = models.CharField(max_length=25)
    desciption = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    old_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.IntegerField(default=0)
    quatity = models.IntegerField(default=0)
    is_delivery = models.BooleanField(default=False)
    slug = models.SlugField(max_length=40, unique=True, blank=False)
    create_at = models.DateField(auto_now=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Order_hotel_food(models.Model):
    user = models.ForeignKey(to='Hotel_food', on_delete=models.CASCADE)
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    dadline = models.DateTimeField()
    create_at = models.DateField(auto_now=True)

class Porkofka(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    number_porkofka = models.IntegerField(unique=True)
    create_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

class Order_porkofka(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    porkofka = models.ForeignKey(to='Porkofka', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=25)
    car_number = models.CharField(max_length=25)
    date = models.DateField()
    create_at = models.DateField(auto_now=True)

class Languge(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Git(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    languge = models.ManyToManyField(to="Languge")
    experience = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to="git_img/")
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

class Order_restaran_food(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    restaran_name  =  models.CharField(max_length=25)
    mean = models.CharField(max_length=35)
    drink = models.CharField(max_length=25)
    quantity = models.IntegerField()
    address = models.CharField(max_length=255)


class Employee(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE)
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Restaran(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    reting = models.FloatField(default=0)
    open_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.CharField(max_length=55)
    img = models.ImageField(upload_to="hotel_img/")
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Table(models.Model):
    restaran = models.ForeignKey(to='Restaran', on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    people_number = models.IntegerField()
    is_delivery = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('small', 'small'),
        ('big', 'big')
    )
    table = models.CharField(max_length=25, choices=TYPE_CHOICES)
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __int__(self):
        return self.number

class Restaran_room(models.Model):
    restaran = models.ForeignKey(to='Restaran', on_delete=models.CASCADE)
    number = models.CharField( max_length=25 ,unique=True)
    people_number = models.IntegerField(default=0)
    is_delivery = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('luks', 'luks'),
        ('simple', 'simple'),
    )
    room = models.CharField(max_length=25, choices=TYPE_CHOICES)
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.number

class Order(models.Model):
    fist_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    address = models.CharField(max_length=55)
    people_number = models.IntegerField()
    is_delivery = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('luks', 'luks'),
        ('simple', 'simple'),
        ('small', 'small'),
        ('big', 'big'),
    )
    room = models.CharField(max_length=25, choices=TYPE_CHOICES)
    date = models.DateField()

class Employee_restaran(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE)
    restaran = models.ForeignKey(to='Restaran', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Mean(models.Model):
    name = models.CharField(max_length=255)
    restaran = models.ForeignKey(to='Restaran', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Sub_category', on_delete=models.PROTECT)
    desciption = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    old_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    quatity = models.IntegerField(default=0)
    craete_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=40, unique=True, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=55)
    craete_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Sub_category(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    craete_at = models.DateField(auto_now=True)


