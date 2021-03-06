# Generated by Django 3.0.2 on 2020-03-15 18:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/access_control/', verbose_name='通过门禁的照片')),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='准确率(%)')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_control_s_person', to=settings.AUTH_USER_MODEL, verbose_name='通过的人')),
            ],
            options={
                'verbose_name': '门禁记录',
                'verbose_name_plural': '门禁记录',
            },
        ),
    ]
