# Generated by Django 4.2.3 on 2023-07-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fcuser",
            name="user_name",
            field=models.CharField(max_length=32, verbose_name="사용자 이름"),
        ),
    ]
