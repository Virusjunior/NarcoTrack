# Generated by Django 4.1.5 on 2023-05-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0009_delete_profile_experience_profile_additional_details_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="additional_details",
            field=models.CharField(default="", max_length=5000),
        ),
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.CharField(default="Your address", max_length=2000),
        ),
        migrations.AlterField(
            model_name="profile",
            name="experience",
            field=models.CharField(default="", max_length=2000),
        ),
    ]
