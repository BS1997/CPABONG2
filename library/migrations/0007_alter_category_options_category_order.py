# Generated by Django 4.2.16 on 2024-12-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0006_category_document_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="category",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
