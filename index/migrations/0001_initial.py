# Generated by Django 3.1.3 on 2020-12-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('footer_image1', models.ImageField(blank='false', upload_to='index/images/footer/')),
                ('footer_image2', models.ImageField(blank='false', upload_to='index/images/footer/')),
                ('footer_contactus_address', models.CharField(max_length=50)),
                ('footer_contactus_phone', models.CharField(max_length=50)),
                ('footer_contactus_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('messege', models.CharField(max_length=100)),
            ],
        ),
    ]
