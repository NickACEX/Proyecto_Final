# Generated by Django 3.1.7 on 2021-04-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('promotion', models.FloatField()),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
