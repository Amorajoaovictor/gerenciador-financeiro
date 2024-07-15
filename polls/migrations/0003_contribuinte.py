# Generated by Django 5.0.1 on 2024-07-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribuinte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('rendaBruta', models.IntegerField()),
                ('contribuicao_previdenciaria', models.IntegerField()),
                ('despesas_medicas', models.IntegerField()),
                ('numero_dependentes', models.IntegerField()),
            ],
        ),
    ]
