# Generated by Django 4.2.5 on 2023-09-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0007_remove_task_important_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='month',
            field=models.CharField(choices=[('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio'), ('JUL', 'Julio'), ('AGO', 'Agosto'), ('SEP', 'Septiembre'), ('OCT', 'Octubre'), ('NOV', 'Noviembre'), ('DIC', 'Diciembre')], default='ENE', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='MEDIA', max_length=15),
        ),
    ]