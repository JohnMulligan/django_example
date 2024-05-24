# Generated by Django 4.2.13 on 2024-05-24 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=100, unique=True)),
                ('card_designation', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('assigned_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees_and_events.card')),
                ('assigned_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees_and_events.department')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.CharField(choices=[('ClockIn', 'Clock In'), ('ClockOut', 'Clock Out')], max_length=20)),
                ('associated_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees_and_events.person')),
                ('card_used', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees_and_events.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='assigned_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees_and_events.department'),
        ),
    ]
