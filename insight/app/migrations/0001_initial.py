# Generated by Django 4.2.2 on 2023-06-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=50, null=True)),
                ('publish_date', models.DateField(null=True)),
                ('category', models.CharField(choices=[('Non-Fiction', 'Non-Fiction'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Autobiography', 'Autobiography'), ('Review', 'Review'), ('Science', 'Science')], max_length=100, null=True)),
            ],
        ),
    ]