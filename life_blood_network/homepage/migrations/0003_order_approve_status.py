# Generated by Django 5.0.6 on 2024-06-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0002_rename_blood_type_order_blood_details_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="approve_status",
            field=models.BooleanField(default=False),
        ),
    ]
