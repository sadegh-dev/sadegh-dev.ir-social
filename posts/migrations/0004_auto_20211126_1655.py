# Generated by Django 3.2.9 on 2021-11-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='craeted',
            new_name='created',
        ),
    ]
