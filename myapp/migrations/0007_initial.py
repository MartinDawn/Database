# Generated by Django 5.0.9 on 2024-11-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0006_delete_nhanvien'),
    ]

    operations = [
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('MaNhanVien', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('SoDienThoai', models.CharField(default='0', max_length=10, unique=True)),
                ('NgayThangNamSinh', models.DateField(default='1')),
                ('NgayBatDauLam', models.DateField(default='1')),
                ('HoTen', models.CharField(default='1', max_length=100)),
                ('GioiTinh', models.CharField(default='nam', max_length=3)),
                ('DiaChi', models.CharField(default='Hồ Chí Minh', max_length=255)),
                ('Email', models.EmailField(default='abc@gmail.com', max_length=100)),
                ('MaQuanLy', models.CharField(default='1', max_length=7, null=True)),
            ],
            options={
                'db_table': 'NhanVien',
            },
        ),
    ]