# Generated by Django 2.2.dev20181016201044 on 2018-10-25 10:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_date', models.DateField(default=django.utils.timezone.now)),
                ('views', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post')),
            ],
        ),
    ]
