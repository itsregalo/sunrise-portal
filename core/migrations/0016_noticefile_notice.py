# Generated by Django 3.2.3 on 2022-01-22 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20220122_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticefile',
            name='notice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.notice'),
            preserve_default=False,
        ),
    ]
