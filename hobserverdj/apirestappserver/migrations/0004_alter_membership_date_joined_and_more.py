# Generated by Django 4.1.3 on 2022-11-19 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apirestappserver", "0003_remove_user_date_created_user_date_joined_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 697390, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="messages",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 698389, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="messages",
            name="updated_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 698389, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 697390, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="updated_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 697390, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 695390, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 695390, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="usersgroups",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 11, 19, 20, 8, 41, 696390, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
