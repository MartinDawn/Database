# Generated by Django 5.0.9 on 2024-11-19 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_nhanvien_email_alter_nhanvien_hoten_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NhanVien',
        ),
    ]