# Generated by Django 4.2.7 on 2023-12-09 11:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_alter_profilesproducts_eat_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profilesproducts",
            old_name="product_id",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="profilesproducts",
            old_name="profile_id",
            new_name="profile",
        ),
    ]
