# Generated by Django 3.2.8 on 2023-01-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_auto_20221227_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='logo',
            field=models.FileField(upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='project'),
        ),
        migrations.AlterField(
            model_name='service',
            name='logo',
            field=models.FileField(upload_to='logo'),
        ),
    ]
