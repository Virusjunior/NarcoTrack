# Generated by Django 4.1.5 on 2023-05-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0008_alter_profile_phone_number"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile_experience",
        ),
        migrations.AddField(
            model_name="profile",
            name="additional_details",
            field=models.CharField(default="", max_length=800),
        ),
        migrations.AddField(
            model_name="profile",
            name="experience",
            field=models.CharField(default="", max_length=500),
        ),
    ]
