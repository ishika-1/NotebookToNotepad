# Generated by Django 3.0.5 on 2020-12-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTNBackEnd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inp_img', models.ImageField(upload_to='input_imgs')),
            ],
        ),
    ]