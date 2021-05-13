# Generated by Django 3.2.2 on 2021-05-13 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_list_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.list')),
            ],
        ),
    ]
