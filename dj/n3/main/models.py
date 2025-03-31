from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    # Choices для различных полей
    BODY_TYPE_CHOICES = [
        ('sedan', 'Седан'),
        ('hatchback', 'Хэтчбек'),
        ('suv', 'Внедорожник'),
        ('coupe', 'Купе'),
        ('minivan', 'Минивэн'),
        ('pickup', 'Пикап'),
    ]
    
    DRIVE_UNIT_CHOICES = [
        ('front', 'Передний'),
        ('rear', 'Задний'),
        ('full', 'Полный'),
    ]
    
    GEARBOX_CHOICES = [
        ('manual', 'Механическая'),
        ('automatic', 'Автоматическая'),
        ('robot', 'Роботизированная'),
        ('variator', 'Вариатор'),
    ]
    
    FUEL_TYPE_CHOICES = [
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electric', 'Электро'),
    ]
    
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    mileage = models.PositiveIntegerField(verbose_name='Пробег (км)')
    volume = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        verbose_name='Объем двигателя (л)',
        validators=[MinValueValidator(0.1)]
    )
    body_type = models.CharField(
        max_length=20, 
        choices=BODY_TYPE_CHOICES, 
        verbose_name='Тип кузова'
    )
    drive_unit = models.CharField(
        max_length=20, 
        choices=DRIVE_UNIT_CHOICES, 
        verbose_name='Привод'
    )
    gearbox = models.CharField(
        max_length=20, 
        choices=GEARBOX_CHOICES, 
        verbose_name='Коробка передач'
    )
    fuel_type = models.CharField(
        max_length=20, 
        choices=FUEL_TYPE_CHOICES, 
        verbose_name='Тип топлива'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Цена',
        validators=[MinValueValidator(0)]
    )
    image = models.ImageField(
        upload_to='cars/images/', 
        verbose_name='Изображение',
        blank=True, 
        null=True
    )
    
    @property
    def formatted_price(self):
        return f"{self.price:,.0f} ₽".replace(",", " ")
    
    def __str__(self):
        return f"{self.model} ({self.year})"
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'



class Sale(models.Model):
    client = models.ForeignKey(
        'Client', 
        on_delete=models.CASCADE, 
        verbose_name='Клиент'
    )
    car = models.ForeignKey(
        Car, 
        on_delete=models.CASCADE, 
        verbose_name='Автомобиль'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата продажи'
    )
    
    def __str__(self):
        return f"Продажа {self.car} клиенту {self.client}"
    
    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
        ordering = ['-created_at']
