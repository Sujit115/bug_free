# Generated by Django 3.0 on 2020-01-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0002_auto_20200116_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]