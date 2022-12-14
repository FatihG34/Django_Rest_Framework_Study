# Generated by Django 4.1.1 on 2022-09-24 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("haberler", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("last_name", models.CharField(max_length=120)),
                ("biography", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="makele",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="makaleler",
                to="haberler.author",
            ),
        ),
    ]
