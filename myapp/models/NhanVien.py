from django.db import models

class NhanVien(models.Model):
    MaNhanVien = models.CharField(max_length=7,primary_key=True)
    SoDienThoai = models.CharField(max_length=10,unique=True,null=False,blank=False,default="0")
    NgayThangNamSinh=models.DateField(null=False,blank=False,default="1")
    NgayBatDauLam=models.DateField(null=False,blank=False,default="1")
    HoTen=models.CharField(max_length=100, null=False,blank=False,default="1")
    GioiTinh=models.CharField(max_length=3,default="nam")
    DiaChi= models.CharField(max_length=255,null=False,blank=False,default="Hồ Chí Minh")
    Email=models.EmailField(max_length=100,null=False,blank=False,default="abc@gmail.com")
    MaQuanLy=models.CharField(max_length=7,null=True,default="1")

    def JSONFY(self):
        data={
            "MaNhanVien":self.MaNhanVien,
            "SoDienThoai":self.SoDienThoai,
            "NgayThangNamSinh":self.NgayThangNamSinh,
            "NgayBatDauLam":self.NgayBatDauLam,
            "HoTen":self.HoTen,
            "GioiTinh":self.GioiTinh,
            "DiaChi":self.DiaChi,
            "Email":self.Email,
            "MaQuanLy":self.MaQuanLy,
        }
        return data
    class Meta: 
        db_table = 'NhanVien'