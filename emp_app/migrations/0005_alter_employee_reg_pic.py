# Generated by Django 4.0.3 on 2022-04-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_rename_image_employee_reg_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_reg',
            name='pic',
            field=models.ImageField(null=True, upload_to='media/', verbose_name=''),
        ),
    ]
