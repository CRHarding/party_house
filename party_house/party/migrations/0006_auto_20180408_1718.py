# Generated by Django 2.0.4 on 2018-04-08 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0005_partyinformation_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partyinformation',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_id', to=settings.AUTH_USER_MODEL),
        ),
    ]