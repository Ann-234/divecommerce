# Generated by Django 4.1.7 on 2023-04-05 06:39

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=225)),
                ('username', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.TextField()),
                ('profile_pix', models.ImageField(default='img/userav.png', upload_to='profile_pix')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
