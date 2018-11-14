# Generated by Django 2.1.3 on 2018-11-14 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('ISBN', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.TextField(max_length=120)),
                ('dept_id', models.TextField(max_length=120)),
                ('buyer', models.CharField(blank=True, max_length=50)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]