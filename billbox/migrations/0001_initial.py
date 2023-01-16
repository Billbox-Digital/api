# Generated by Django 4.1.5 on 2023-01-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billboxcode', models.CharField(max_length=12, null=True)),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(max_length=255, null=True)),
                ('address3', models.CharField(max_length=255, null=True)),
                ('zipcode', models.CharField(max_length=32, null=True)),
                ('postalcode', models.CharField(max_length=32, null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('phone', models.BigIntegerField(default=0)),
                ('user', models.BigIntegerField(default=0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='billbox.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='billbox.country')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='billbox.state')),
            ],
        ),
    ]