# Generated by Django 4.1.1 on 2022-09-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JGChain', '0002_alter_block_current_hash_alter_block_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='current_hash',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='block',
            name='previous_hash',
            field=models.CharField(max_length=64),
        ),
    ]
