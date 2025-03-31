# Generated by Django 3.1.2 on 2025-03-31 08:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег (км)')),
                ('volume', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Объем двигателя (л)')),
                ('body_type', models.CharField(choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('suv', 'Внедорожник'), ('coupe', 'Купе'), ('minivan', 'Минивэн'), ('pickup', 'Пикап')], max_length=20, verbose_name='Тип кузова')),
                ('drive_unit', models.CharField(choices=[('front', 'Передний'), ('rear', 'Задний'), ('full', 'Полный')], max_length=20, verbose_name='Привод')),
                ('gearbox', models.CharField(choices=[('manual', 'Механическая'), ('automatic', 'Автоматическая'), ('robot', 'Роботизированная'), ('variator', 'Вариатор')], max_length=20, verbose_name='Коробка передач')),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electric', 'Электро')], max_length=20, verbose_name='Тип топлива')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car', verbose_name='Автомобиль')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажи',
                'ordering': ['-created_at'],
            },
        ),
    ]
