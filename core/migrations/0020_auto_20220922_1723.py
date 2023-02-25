# Generated by Django 3.2.9 on 2022-09-22 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_delete_tournamentregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('surnames', models.CharField(max_length=100, verbose_name='apellidos')),
                ('mail', models.EmailField(max_length=100, verbose_name='correo electrónico')),
                ('population', models.CharField(max_length=100, verbose_name='población')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Código Postal')),
                ('date_birth', models.DateTimeField(verbose_name='fecha de nacimiento')),
                ('phone', models.CharField(max_length=15, verbose_name='teléfono')),
                ('status', models.CharField(max_length=100, verbose_name='estado')),
                ('privacy_policy', models.BooleanField(default=False, verbose_name='Aceptar política privacidad')),
                ('tournament_title', models.CharField(max_length=200, verbose_name='nombre del torneo')),
                ('paid', models.BooleanField(default=False, verbose_name='pagado')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.torneo', verbose_name='torneo')),
            ],
            options={
                'verbose_name_plural': 'registros',
                'ordering': ['-surnames'],
            },
        ),
        migrations.AddConstraint(
            model_name='tournamentregistration',
            constraint=models.UniqueConstraint(fields=('name', 'surnames', 'mail', 'tournament_title'), name='unique_tournamentregistration'),
        ),
    ]
