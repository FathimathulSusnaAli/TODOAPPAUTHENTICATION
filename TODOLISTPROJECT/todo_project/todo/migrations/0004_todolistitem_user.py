# Generated by Django 4.1.3 on 2022-11-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todolistitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='user',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
    ]
