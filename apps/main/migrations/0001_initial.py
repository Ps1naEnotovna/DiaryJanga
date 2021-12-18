# Generated by Django 4.0 on 2021-12-18 09:40

import apps.accordant_utils.base_model
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
            bases=(models.Model, apps.accordant_utils.base_model.CUDateModel),
        ),
    ]
