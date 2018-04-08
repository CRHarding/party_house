# Generated by Django 2.0.4 on 2018-04-08 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_attended', models.IntegerField(blank=True, help_text="Number of parties that you've attended")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='partyinformation',
            name='address_city',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]