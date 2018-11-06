# Generated by Django 2.2.dev20181016201044 on 2018-11-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Draft'), ('a', 'Available'), ('r', 'Reserved')], default='d', help_text='Post availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(help_text='Select a category for this post', to='blog.Category'),
        ),
    ]