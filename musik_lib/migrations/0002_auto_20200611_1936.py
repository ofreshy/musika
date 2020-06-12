# Generated by Django 3.0.7 on 2020-06-11 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musik_lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackInCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveSmallIntegerField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musik_lib.Collection')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musik_lib.Track')),
            ],
        ),
        migrations.AddConstraint(
            model_name='trackincollection',
            constraint=models.UniqueConstraint(fields=('collection', 'ordinal'), name='Collection and Ordinal'),
        ),
    ]
