# Generated by Django 5.0.1 on 2024-01-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boardapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boardmodel",
            name="good",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="boardmodel",
            name="read",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="boardmodel",
            name="read_text",
            field=models.TextField(blank=True, null=True),
        ),
    ]