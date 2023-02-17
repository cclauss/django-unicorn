# Generated by Django 3.2.16 on 2023-02-14 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_auto_20221110_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(default=False)),
                ('flavor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='coffee.flavor')),
            ],
        ),
    ]