# Generated by Django 2.2.4 on 2020-01-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcomment',
            name='approved_comment',
        ),
        migrations.RemoveField(
            model_name='addcomment',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=10),
        ),
    ]
