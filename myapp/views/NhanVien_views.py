from django.http import JsonResponse, HttpResponse
from ..repositories import NhanVienRepository  
import json
from django.views.decorators.csrf import csrf_exempt
# --------------------NhanVien-----------------------------------------------
#--------------------------------read----------------------------------------
def read_all_NhanVien(request):
    if request.method =='GET':
        try: 
            data = NhanVienRepository.NhanVien.read_all_NhanVien()
            data = json.loads(data)
            return JsonResponse({"NhanVien": data}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau.'}, status=500)
    else :
        return HttpResponse(status=405)
    
def read_fulltime_NhanVien(request):
    if request.method=='GET':
        data =NhanVienRepository.NhanVien.read_fulltime_NhanVien()
        return JsonResponse({"NhanVien":data},status=200)
    else:
        return HttpResponse(status=405)
def read_parttime_NhanVien(request):
    if request.method=='GET':
        data =NhanVienRepository.NhanVien.read_parttime_NhanVien()
        return JsonResponse({"NhanVien":data},status=200)
    else:
        return HttpResponse(status=405)
@csrf_exempt  
def read_one_NhanVien(request):
    if request.method =='POST':
        try: 
            data=json.loads(request.body)
            data = NhanVienRepository.NhanVien.read_one_NhanVien(data.get('data'))
            data = json.loads(data)
            return JsonResponse({"NhanVien": data}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau.'}, status=500)
    else :
        return HttpResponse(status=405)
@csrf_exempt  
def read_one_parttime_NhanVien(request):
    if request.method == 'POST':
            data=json.loads(request.body)
            data= NhanVienRepository.NhanVien.read_one_parttime_NhanVien(data.get('data'))
            return JsonResponse({"NhanVien":data},status=200)
        
    else:
        return HttpResponse(status=405)
@csrf_exempt  
def read_one_fulltime_NhanVien(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        data= NhanVienRepository.NhanVien.read_one_fulltime_NhanVien(data.get('data'))
        return JsonResponse({"NhanVien":data},status=200)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def update_NhanVien(request):
    if request.method=='POST':
        data= json.loads(request.body)

    else:
        return HttpResponse(status=405)

# --------------------KhachHang-----------------------------------------------


@csrf_exempt
def them_nhan_vien(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            NhanVienRepository.NhanVien.them_nhan_vien(
                data.get('MaNhanVien'),
                data.get('SoDienThoai'),
                data.get('NgayThangNamSinh'),
                data.get('NgayBatDauLam'),
                data.get('HoTen'),
                data.get('GioiTinh'),
                data.get('DiaChi'),
                data.get('Email'),
                data.get('MaQuanLy'),
                data.get('CanCuocCongDan')
            )
            return JsonResponse({'message': 'Nhân viên đã được thêm thành công'}, status=200)
        except Exception as e:
            e = str(e) # Tìm phần giữa của thông báo lỗi 
            error_start = e.find('[SQL Server]') + len('[SQL Server]') 
            error_end = e.find('(50000)', error_start) 
            e = e[error_start:error_end].strip() 
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Phương thức không hợp lệ'}, status=405)

@csrf_exempt
def sua_nhan_vien(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            NhanVienRepository.NhanVien.sua_nhan_vien(
                data.get('MaNhanVien'),
                data.get('SoDienThoai'),
                data.get('NgayThangNamSinh'),
                data.get('NgayBatDauLam'),
                data.get('HoTen'),
                data.get('GioiTinh'),
                data.get('DiaChi'),
                data.get('Email'),
                data.get('MaQuanLy'),
                data.get('CanCuocCongDan')
            )
            return JsonResponse({'message': 'Thông tin nhân viên đã được cập nhật thành công'}, status=200)
        except Exception as e:
            e = str(e) # Tìm phần giữa của thông báo lỗi 
            error_start = e.find('[SQL Server]') + len('[SQL Server]') 
            error_end = e.find('(50000)', error_start) 
            e = e[error_start:error_end].strip() 
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Phương thức không hợp lệ'}, status=405)


@csrf_exempt
def xoa_nhan_vien(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            NhanVienRepository.NhanVien.xoa_nhan_vien(data.get('MaNhanVien'))
            return JsonResponse({'message': 'Nhân viên đã được xóa thành công'}, status=200)
        except Exception as e:
            e = str(e) # Tìm phần giữa của thông báo lỗi 
            error_start = e.find('[SQL Server]') + len('[SQL Server]') 
            error_end = e.find('(50000)', error_start) 
            e = e[error_start:error_end].strip() 
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Phương thức không hợp lệ'}, status=405)
