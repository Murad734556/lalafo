# Generated by Django 4.0.5 on 2022-07-24 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveBigIntegerField(default=0, verbose_name='Рейтинг')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status_comment', models.CharField(choices=[('В ожидании', 'В ожидании'), ('Не принято', 'Не принято'), ('Принято', 'Принято')], default='В ожидании', max_length=30, verbose_name='Статус комментария')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_for_user', to=settings.AUTH_USER_MODEL, verbose_name='К пользователю')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='От пользователя')),
            ],
            options={
                'verbose_name': 'Комментарий пользователю',
                'verbose_name_plural': 'Комментарии пользователям',
            },
        ),
    ]
