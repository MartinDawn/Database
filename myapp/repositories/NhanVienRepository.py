from django.db import connection
import os, json
from decimal import Decimal
from datetime import date
class NhanVien:
    # --------------------read----------------------------------------------------
    @staticmethod
    def read_all_NhanVien():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM NhanVien")
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
                    if isinstance(value, date):
                        item[key] = value.strftime('%Y-%m-%d')
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json

    @staticmethod
    def read_one_NhanVien(id):  
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM NhanVien \
                           where MaNhanVien = %s",(id, ))
            result = cursor.fetchall()
            print(result)
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
                    if isinstance(value, date):
                        item[key] = value.strftime('%Y-%m-%d')
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json
    
    @staticmethod
    def read_fulltime_NhanVien():
        with connection .cursor() as cursor:
            cursor.execute("\
            SELECT * FROM NhanVien x, NhanVienFullTime y\
                           where x.MaNhanVien= y.MaNhanVien\
                           ")
            result = cursor.fetchall()
            return result
        
    @staticmethod
    def read_parttime_NhanVien():
        with connection .cursor() as cursor:
            cursor.execute("\
SELECT * FROM NhanVien x, NhanVienPartTime y\
                           where x.MaNhanVien= y.MaNhanVien\
                           ")
            result = cursor.fetchall()
            return result
        
    @staticmethod
    def read_one_parttime_NhanVien(id):
        with connection .cursor() as cursor:
            cursor.execute("SELECT * FROM NhanVien x, NhanVienPartTime y where x.MaNhanVien= y.MaNhanVien and x.MaNhanVien=%s", [id])
            result = cursor.fetchall()
            return result
        
    @staticmethod
    def read_one_fulltime_NhanVien(id):
        with connection .cursor() as cursor:
            cursor.execute("SELECT * FROM NhanVien x, NhanVienFullTime \
                y where x.MaNhanVien= y.MaNhanVien and x.MaNhanVien=%s", [id])
            result = cursor.fetchall()
            return result
    # ------------------------------------create-------------------------------


# ---------------------------------hang hoa------------------------------------
    @staticmethod
    def them_nhan_vien(ma_nhan_vien, so_dien_thoai, ngay_thang_nam_sinh, ngay_bat_dau_lam, ho_ten, gioi_tinh, dia_chi, email, ma_quan_ly, can_cuoc_cong_dan):
        with connection.cursor() as cursor:
            query = """
                EXEC ThemNhanVien @MaNhanVien=%s, @SoDienThoai=%s, @NgayThangNamSinh=%s, @NgayBatDauLam=%s,
                                  @HoTen=%s, @GioiTinh=%s, @DiaChi=%s, @Email=%s, @MaQuanLy=%s, @CanCuocCongDan=%s
            """
            cursor.execute(query, [ma_nhan_vien, so_dien_thoai, ngay_thang_nam_sinh, ngay_bat_dau_lam, ho_ten, gioi_tinh, dia_chi, email, ma_quan_ly, can_cuoc_cong_dan])

    @staticmethod
    def sua_nhan_vien(ma_nhan_vien, so_dien_thoai=None, ngay_thang_nam_sinh=None, ngay_bat_dau_lam=None, ho_ten=None, gioi_tinh=None, dia_chi=None, email=None, ma_quan_ly=None, can_cuoc_cong_dan=None):
        with connection.cursor() as cursor:
            query = """
                EXEC SuaNhanVien @MaNhanVien=%s, @SoDienThoai=%s, @NgayThangNamSinh=%s, @NgayBatDauLam=%s,
                                 @HoTen=%s, @GioiTinh=%s, @DiaChi=%s, @Email=%s, @MaQuanLy=%s, @CanCuocCongDan=%s
            """
            cursor.execute(query, [ma_nhan_vien, so_dien_thoai, ngay_thang_nam_sinh, ngay_bat_dau_lam, ho_ten, gioi_tinh, dia_chi, email, ma_quan_ly, can_cuoc_cong_dan])

   
    @staticmethod
    def xoa_nhan_vien(ma_nhan_vien):
        with connection.cursor() as cursor:
            query = "EXEC XoaNhanVien @MaNhanVien=%s"
            cursor.execute(query, [ma_nhan_vien])
