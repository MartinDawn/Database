from django.db import connection
import os, json
import pyodbc
from datetime import date, datetime
from decimal import Decimal
class HangHoa:
    # -------------------read-----------------------------------------
    @staticmethod#okk
    def readAllMerchandise():
        with connection.cursor() as cursor:
            cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh,H.SoLuongConLai, L.MaLoai, L.TenLoai \
                            FROM HangHoa H, Loai L \
                            WHERE H.MaLoai = L.MaLoai \
            ")
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json

    @staticmethod#okk
    def readAllMerchandiseAsIncr():
        with connection.cursor() as cursor:
                cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh,H.SoLuongConLai, L.MaLoai, L.TenLoai \
                                FROM HangHoa H, Loai L \
                                WHERE H.MaLoai = L.MaLoai \
                                    order by H.Gia asc")
                result = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                result_as_dict = [dict(zip(columns, row)) for row in result]
                for item in result_as_dict:
                    for key, value in item.items():
                        if isinstance(value, Decimal):
                            item[key] = float(value)
                result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
                return result_as_json
    @staticmethod#okk
    def readAllMerchandiseAsDesc():
        with connection.cursor() as cursor:
                cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh,H.SoLuongConLai, L.MaLoai, L.TenLoai \
                                FROM HangHoa H, Loai L \
                                WHERE H.MaLoai = L.MaLoai \
                                    order by H.Gia desc")
                result = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                result_as_dict = [dict(zip(columns, row)) for row in result]
                for item in result_as_dict:
                    for key, value in item.items():
                        if isinstance(value, Decimal):
                            item[key] = float(value)
                result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
                return result_as_json
    @staticmethod#okk
    def readMerchandiseAsType(type):
        with connection.cursor() as cursor:
            cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh, H.SoLuongConLai, L.MaLoai, L.TenLoai \
                            FROM HangHoa H, Loai L \
                            WHERE H.MaLoai = L.MaLoai and L.Tenloai =%s ", (type,))
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json
    @staticmethod#okk
    def readMerchandiseAsTypeAsDesc(type):
        with connection.cursor() as cursor:
            cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh, H.SoLuongConLai, L.MaLoai, L.TenLoai \
                            FROM HangHoa H, Loai L \
                            WHERE H.MaLoai = L.MaLoai and L.Tenloai =%s \
                            order by H.Gia Desc", (type,))
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json
    @staticmethod#okk
    def readMerchandiseAsTypeAsIncr(type):
        with connection.cursor() as cursor:
            cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh, H.SoLuongConLai, L.MaLoai, L.TenLoai \
                            FROM HangHoa H, Loai L \
                            WHERE H.MaLoai = L.MaLoai and L.Tenloai =%s \
                            order by H.Gia Asc", (type,))
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json
    
    @staticmethod#okk
    def readMerchandiseAsId(id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT H.MaHangHoa, H.Ten, H.Gia, H.DonViTinh, H.SoLuongConLai, L.MaLoai, L.TenLoai \
                            FROM HangHoa H, Loai L \
                            WHERE H.MaLoai = L.MaLoai and H.MaHangHoa =%s \
                            ", (id,))
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json
        


    @staticmethod
    def readShipmentAsMerchandiseId(id):
        with connection.cursor() as cursor:
            cursor.execute("select C.MaHangHoa, C.MaLoHang, C.SoLuongHangHoa,\
                           N.DiaChi,N.Email,N.MaNhaCungCap,N.SoDienThoai,N.Ten\
  from LoHang L, Chua C, NhaCungCap N\
  where L.MaLoHang=C.MaLoHang and C.MaNhaCungCap=N.MaNhaCungCap and C.MaHangHoa = %s",(id,))
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        item[key] = float(value)
            result_as_json = json.dumps(result_as_dict, ensure_ascii=False)
            return result_as_json



    #  -------------delete--------------------------------------------
    @staticmethod
    def delete_one_HangHoa(id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM HangHoa WHERE MaHangHoa = %s", [id])
                rowcount = cursor.rowcount
            return rowcount > 0  # Trả về True nếu có bản ghi bị xóa, ngược lại là False
        except Exception as e:
            print(f"Database error: {e}")
        return False  # Trả về False nếu có lỗi xảy ra
    # ----------------------------create------------------------------
    @staticmethod
    def create_one_HangHoa(Ma_hang_hoa, Ten, Gia, Loai, DonViTinh, SoLuongConLai):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO HangHoa (MaHangHoa, Ten, Gia, MaLoai, DonViTinh, SoLuongConLai) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """, [Ma_hang_hoa, Ten, Gia, Loai, DonViTinh, SoLuongConLai])
            return True  
        except Exception as e:
            print(f"Database error: {e}")
            return False  
    
    @staticmethod
    def update_one_HangHoa(Ma_hang_hoa, Ten=None, Gia=None, Loai=None, DonViTinh=None, SoLuongConLai=None):
        try:
            with connection.cursor() as cursor:
                update_fields = []
                update_values = []

                if Ten is not None:
                    update_fields.append("Ten = %s")
                    update_values.append(Ten)
                if Gia is not None:
                    update_fields.append("Gia = %s")
                    update_values.append(Gia)
                if Loai is not None:
                    update_fields.append("MaLoai = %s")
                    update_values.append(Loai)
                if DonViTinh is not None:
                    update_fields.append("DonViTinh = %s")
                    update_values.append(DonViTinh)
                if SoLuongConLai is not None:
                    update_fields.append("SoLuongConLai = %s")
                    update_values.append(SoLuongConLai)

                # Chỉ thực hiện cập nhật nếu có bất kỳ trường nào cần cập nhật
                if update_fields:
                    update_values.append(Ma_hang_hoa)
                    update_query = f"UPDATE HangHoa SET {', '.join(update_fields)} WHERE MaHangHoa = %s"
                    cursor.execute(update_query, update_values)
                    return True
                else:
                    return False  # Không có trường nào để cập nhật
        except Exception as e:
            print(f"Database error: {e}")
            return False
    
# ------------------------------------------New---------------------------------------
# HANG HOA MERCHANDISE
        
    @staticmethod
    def hien_thi_hoa_don_khach_hang(ngay_bat_dau, ngay_ket_thuc):
        with connection.cursor() as cursor:
            query = "EXEC HienThiHoaDonKhachHang @NgayBatDau = %s, @NgayKetThuc = %s"
            cursor.execute(query, [ngay_bat_dau, ngay_ket_thuc])
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result_as_dict = [dict(zip(columns, row)) for row in result]
            
            # Chuyển đổi date thành chuỗi
            for item in result_as_dict:
                for key, value in item.items():
                    if isinstance(value, date):
                        item[key] = value.strftime('%Y-%m-%d')
                    elif isinstance(value, datetime):
                        item[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            
            return json.dumps(result_as_dict, ensure_ascii=False)
