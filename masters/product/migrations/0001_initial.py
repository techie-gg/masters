# Generated by Django 2.0 on 2020-07-03 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='product.Category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'verbose_name': 'Sub Category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_category', to='product.SubCategory'),
        ),
    ]