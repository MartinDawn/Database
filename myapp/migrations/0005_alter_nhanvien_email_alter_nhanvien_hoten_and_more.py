# Generated by Django 5.0.9 on 2024-11-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_nhanvien_diachi_nhanvien_gioitinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhanvien',
            name='Email',
            field=models.EmailField(default='abc@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='HoTen',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='MaQuanLy',
            field=models.CharField(default='1', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='NgayBatDauLam',
            field=models.DateField(default='1'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='NgayThangNamSinh',
            field=models.DateField(default='1'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='SoDienThoai',
            field=models.CharField(default='0', max_length=10, unique=True),
        ),
    ]
