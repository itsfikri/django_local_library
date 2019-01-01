# Generated by Django 2.1.3 on 2018-12-24 01:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181221_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Died'),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]