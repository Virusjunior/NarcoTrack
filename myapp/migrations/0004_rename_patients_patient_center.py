# Generated by Django 4.1.5 on 2023-05-18 14:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_rename_patient_patients"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Patients",
            new_name="Patient",
        ),
        migrations.CreateModel(
            name="Center",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("orgranization_name", models.CharField(max_length=200)),
                ("mode_of_organization", models.CharField(max_length=200)),
                ("description", ckeditor.fields.RichTextField()),
                (
                    "Profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.profile"
                    ),
                ),
            ],
        ),
    ]
