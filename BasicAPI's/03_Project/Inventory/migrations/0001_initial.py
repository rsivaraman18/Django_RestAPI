# Generated by Django 4.2.14 on 2024-07-20 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myproducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('code', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(default=0)),
                ('category_refrences', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventory.productcategory')),
            ],
        ),
    ]
