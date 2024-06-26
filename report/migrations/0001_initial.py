# Generated by Django 5.0.6 on 2024-05-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_count', models.FloatField()),
                ('application_count_filtered', models.FloatField()),
                ('duplicate_count', models.FloatField()),
                ('duplicate_count_filtered', models.FloatField()),
                ('addition_count', models.FloatField()),
                ('addition_count_filtered', models.FloatField()),
                ('extension_count', models.FloatField()),
                ('extension_count_filtered', models.FloatField()),
                ('pending_count', models.FloatField()),
                ('pending_count_filtered', models.FloatField()),
                ('processing_count', models.FloatField()),
                ('processing_count_filtered', models.FloatField()),
                ('package_count', models.FloatField()),
                ('package_count_filtered', models.FloatField()),
                ('success_processing_count', models.FloatField()),
                ('success_processing_count_filtered', models.FloatField()),
                ('auth_count', models.FloatField()),
                ('auth_count_filtered', models.FloatField()),
            ],
        ),
    ]
