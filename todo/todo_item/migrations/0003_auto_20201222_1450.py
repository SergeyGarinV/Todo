# Generated by Django 3.1.4 on 2020-12-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_item', '0002_auto_20201213_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='expr_date',
            field=models.DateTimeField(null=True),
        ),
    ]
