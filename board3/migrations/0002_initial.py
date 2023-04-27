# Generated by Django 4.2 on 2023-04-26 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boardmapping', '__first__'),
        ('board3', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='board3',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board3',
            name='board_mapping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='board3', to='boardmapping.boardmapping'),
        ),
    ]