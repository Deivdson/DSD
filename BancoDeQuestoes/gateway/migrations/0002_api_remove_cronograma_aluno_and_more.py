# Generated by Django 4.1.4 on 2023-01-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='cronograma',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='cronograma',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Dailyschedule',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='cronograma',
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
        migrations.DeleteModel(
            name='Cronograma',
        ),
        migrations.DeleteModel(
            name='Tarefa',
        ),
    ]
