# Generated by Django 5.1.7 on 2025-03-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id_editorial', models.AutoField(db_column='T002IdEditorial', editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='T002Nombre', max_length=100)),
                ('direccion', models.CharField(db_column='T002Direccion', max_length=80)),
                ('telefono', models.CharField(blank=True, db_column='T002Telefono', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
                'db_table': 'T002',
            },
        ),
        migrations.AlterField(
            model_name='autor',
            name='biografia',
            field=models.CharField(blank=True, db_column='T001Biografia', max_length=200, null=True),
        ),
    ]
