# Generated by Django 3.2 on 2022-12-09 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.image'),
        ),
        migrations.AlterField(
            model_name='productlubricant',
            name='volume',
            field=models.CharField(blank=True, choices=[('barrel', 'barrel'), ('canister', 'canister'), ('other', 'other')], max_length=255, null=True),
        ),
    ]