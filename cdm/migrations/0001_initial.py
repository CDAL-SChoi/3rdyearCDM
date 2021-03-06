# Generated by Django 3.2.9 on 2021-11-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionOccurrence',
            fields=[
                ('condition_occurrence_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('person_id', models.BigIntegerField()),
                ('condition_concept_id', models.IntegerField()),
                ('condition_start_date', models.DateField()),
                ('condition_start_datetime', models.DateTimeField(blank=True, null=True)),
                ('condition_end_date', models.DateField(blank=True, null=True)),
                ('condition_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('condition_type_concept_id', models.IntegerField()),
                ('stop_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_occurrence_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_detail_id', models.BigIntegerField(blank=True, null=True)),
                ('condition_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('condition_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('condition_status_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('condition_status_concept_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'condition_occurrence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.BigIntegerField()),
                ('death_date', models.DateField()),
                ('death_datetime', models.DateTimeField(blank=True, null=True)),
                ('death_type_concept_id', models.IntegerField()),
                ('cause_concept_id', models.IntegerField(blank=True, null=True)),
                ('cause_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('cause_source_concept_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'death',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.BigIntegerField()),
                ('gender_concept_id', models.IntegerField()),
                ('year_of_birth', models.IntegerField()),
                ('month_of_birth', models.IntegerField(blank=True, null=True)),
                ('day_of_birth', models.IntegerField(blank=True, null=True)),
                ('birth_datetime', models.DateTimeField(blank=True, null=True)),
                ('race_concept_id', models.IntegerField()),
                ('ethnicity_concept_id', models.IntegerField()),
                ('location_id', models.IntegerField(blank=True, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('care_site_id', models.IntegerField(blank=True, null=True)),
                ('person_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gender_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gender_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('race_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('race_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('ethnicity_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('ethnicity_source_concept_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcedureOccurrence',
            fields=[
                ('procedure_occurrence_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('person_id', models.BigIntegerField()),
                ('procedure_concept_id', models.IntegerField()),
                ('procedure_date', models.DateField()),
                ('procedure_datetime', models.DateTimeField(blank=True, null=True)),
                ('procedure_type_concept_id', models.IntegerField()),
                ('modifier_concept_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_occurrence_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_detail_id', models.BigIntegerField(blank=True, null=True)),
                ('procedure_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('procedure_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('modifier_source_value', models.IntegerField()),
            ],
            options={
                'db_table': 'procedure_occurrence',
                'managed': False,
            },
        ),
    ]
