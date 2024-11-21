from django.http import JsonResponse, HttpResponse
from ..repositories import NhanVienRepository  
import json
from django.views.decorators.csrf import csrf_exempt
# --------------------NhanVien-----------------------------------------------
#--------------------------------read----------------------------------------
def read_all_NhanVien(request):
    if request.method =='GET':
        data = NhanVienRepository.NhanVien.read_all_NhanVien()
        
        return JsonResponse({"NhanVien": data}, status=200)
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
        data = json.loads(request.body)
        data = NhanVienRepository.NhanVien.read_one_NhanVien(data.get('data'))
        
        return JsonResponse({"NhanVien": data}, status=200)
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