# Generated by Django 5.1.5 on 2025-02-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_faq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
    ]
