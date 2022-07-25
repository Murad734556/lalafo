# Generated by Django 4.0.5 on 2022-07-24 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_aboutus_blog_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='contact',
            name='problem_en',
            field=models.TextField(null=True, verbose_name='Проблема'),
        ),
        migrations.AddField(
            model_name='contact',
            name='problem_ru',
            field=models.TextField(null=True, verbose_name='Проблема'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status_en',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('Решена', 'Решена'), ('Не решена', 'Не решена')], default='В ожидании', max_length=30, null=True, verbose_name='Статус обращения'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status_ru',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('Решена', 'Решена'), ('Не решена', 'Не решена')], default='В ожидании', max_length=30, null=True, verbose_name='Статус обращения'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='setting',
            name='address_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='setting',
            name='address_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='setting',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание сайта'),
        ),
        migrations.AddField(
            model_name='setting',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание сайта'),
        ),
        migrations.AddField(
            model_name='setting',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название сайта'),
        ),
        migrations.AddField(
            model_name='setting',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название сайта'),
        ),
    ]