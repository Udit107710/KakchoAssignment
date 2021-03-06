# Generated by Django 2.2.1 on 2019-05-28 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/first')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/original')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecondTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/second')),
                ('firsttask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.FirstTaskModel')),
            ],
        ),
        migrations.CreateModel(
            name='RoundOffModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/roundoff')),
                ('uploadfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UploadFileModel')),
            ],
        ),
        migrations.AddField(
            model_name='firsttaskmodel',
            name='uploadfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UploadFileModel'),
        ),
    ]
