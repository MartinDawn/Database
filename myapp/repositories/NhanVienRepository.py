from django.db import connection
import os
class NhanVien:
    # --------------------read----------------------------------------------------
    @staticmethod
    def read_all_NhanVien():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM NhanVien")
            result = cursor.fetchall()
            return result


    @staticmethod
    def read_one_NhanVien(id):  
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM NhanVien WHERE MaNhanVien = %s", [id])
            result = cursor.fetchall()
            return result
    
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
