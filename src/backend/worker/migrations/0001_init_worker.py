# Generated by Django 3.1.7 on 2021-03-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('function_name', models.CharField(choices=[], help_text='function will be called', max_length=50)),
                ('state', models.CharField(choices=[('QD', 'queued'), ('PR', 'in progress'), ('ER', 'error'), ('CM', 'completed')], default='QD', help_text='task state', max_length=10)),
                ('logs', models.JSONField(blank=True, default=dict, null=True)),
                ('message', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
    ]