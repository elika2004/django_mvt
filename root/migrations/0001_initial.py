# Generated by Django 4.2 on 2024-10-30 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='defult.jpg', upload_to='agent')),
                ('twiter', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('insagram', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=False)),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.ability')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
