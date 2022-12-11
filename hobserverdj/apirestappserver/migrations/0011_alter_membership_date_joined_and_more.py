# Generated by Django 4.1.3 on 2022-12-07 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apirestappserver", "0010_alter_membership_date_joined_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 504286, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="messages",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 504286, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="messages",
            name="updated_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 504286, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 504286, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="updated_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 504286, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 501285, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 501285, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="image_url",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="usersgroups",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 12, 7, 19, 15, 8, 503285, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]