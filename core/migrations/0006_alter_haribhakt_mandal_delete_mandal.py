# Generated by Django 4.2.8 on 2024-08-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_mandal_khestra"),
        ("mandal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="haribhakt",
            name="mandal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mandal.mandal",
            ),
        ),
        migrations.DeleteModel(
            name="Mandal",
        ),
    ]
