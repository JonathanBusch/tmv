# Generated by Django 2.1.2 on 2019-02-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0016_twittersearch_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='text',
            field=models.TextField(db_index=True, null=True),
        ),
    ]
