# Generated by Django 4.1.5 on 2023-02-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(choices=[('2', 'Lv2_사용자'), ('1', 'Lv1_관리자'), ('0', 'Lv0_개발자')], default=1, max_length=4, verbose_name='지자체코드'),
        ),
    ]
