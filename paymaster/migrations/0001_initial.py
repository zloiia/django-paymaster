# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=17, unique=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0447\u0435\u0442\u0430')),
                ('description', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043b\u0430\u0442\u0435\u0436\u0430')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='\u0421\u0443\u043c\u043c\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430, \u0437\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u043c')),
                ('currency', models.CharField(max_length=3, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430, \u0437\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u043c')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='\u0421\u0443\u043c\u043c\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430 \u0432 \u0432\u0430\u043b\u044e\u0442\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442 \u043f\u043b\u0430\u0442\u0435\u0436')),
                ('paid_currency', models.CharField(max_length=3, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u043f\u043b\u0430\u0442\u0435\u0436')),
                ('payment_method', models.CharField(max_length=50, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043b\u0430\u0442\u0435\u0436\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b, \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0435\u043c')),
                ('payment_system', models.CharField(max_length=50, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043b\u0430\u0442\u0435\u0436\u043d\u043e\u0433\u043e \u043c\u0435\u0442\u043e\u0434\u0430')),
                ('payment_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u043b\u0430\u0442\u0435\u0436\u0430 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 PayMaster')),
                ('payer_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a\u0430 \u0432 \u043f\u043b\u0430\u0442\u0435\u0436\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u0435')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438')),
                ('edition_date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0421\u0447\u0435\u0442',
                'verbose_name_plural': '\u0421\u0447\u0435\u0442\u0430',
            },
        ),
    ]
