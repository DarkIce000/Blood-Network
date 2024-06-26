# Generated by Django 5.0.6 on 2024-06-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0003_order_approve_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="cancel_status",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="rejected_status",
            field=models.BooleanField(default=False),
        ),
    ]
