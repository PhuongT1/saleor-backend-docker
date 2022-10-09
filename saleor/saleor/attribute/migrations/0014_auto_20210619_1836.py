# Generated by Django 3.2.4 on 2021-06-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attribute", "0013_auto_20210609_2245"),
    ]

    operations = [
        migrations.AddField(
            model_name="attributevalue",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="attribute",
            name="input_type",
            field=models.CharField(
                choices=[
                    ("dropdown", "Dropdown"),
                    ("multiselect", "Multi Select"),
                    ("file", "File"),
                    ("reference", "Reference"),
                    ("numeric", "Numeric"),
                    ("rich-text", "Rich Text"),
                    ("boolean", "Boolean"),
                    ("date", "Date"),
                    ("date-time", "Date Time"),
                ],
                default="dropdown",
                max_length=50,
            ),
        ),
    ]
