# Generated by Django 5.2.4 on 2025-07-05 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("managers", "0007_alter_projects_star_project_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects_star",
            name="project_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="managers.projects"
            ),
        ),
    ]
