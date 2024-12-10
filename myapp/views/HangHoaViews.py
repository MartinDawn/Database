from django.http import JsonResponse, HttpResponse
from ..repositories import NhanVienRepository, HangHoaRepository
import json
from django.views.decorators.csrf import csrf_exempt

def readAllMerchandise(request):
    if request.method =='GET':
        try:
            data = HangHoaRepository.HangHoa.readAllMerchandise()
            data = json.loads(data)
            return JsonResponse({'HangHoa':data}, status=200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)
    
def readAllMerchandiseAsIncr(request):
    if request.method =='GET':
        try:
            data = HangHoaRepository.HangHoa.readAllMerchandiseAsIncr()
            data = json.loads(data)
            return JsonResponse({'HangHoa':data}, status=200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)
def readAllMerchandiseAsDesc(request):
    if request.method =='GET':
        try:
            data = HangHoaRepository.HangHoa.readAllMerchandiseAsDesc()
            data = json.loads(data)
            return JsonResponse({'HangHoa':data}, status=200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)
@csrf_exempt
def readMerchandiseAsType(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            data= HangHoaRepository.HangHoa.readMerchandiseAsType(data.get('type'))
            data=json.loads(data)
            return JsonResponse({'HangHoa':data},status = 200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)

@csrf_exempt
def readMerchandiseAsTypeAsDesc(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            data= HangHoaRepository.HangHoa.readMerchandiseAsTypeAsDesc(data.get('type'))
            data=json.loads(data)
            return JsonResponse({'HangHoa':data},status = 200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)
@csrf_exempt
def readMerchandiseAsTypeAsIncr(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            data= HangHoaRepository.HangHoa.readMerchandiseAsTypeAsIncr(data.get('type'))
            data=json.loads(data)
            return JsonResponse({'HangHoa':data},status = 200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)

@csrf_exempt
def readMerchandiseAsId(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            
            data= HangHoaRepository.HangHoa.readMerchandiseAsId(data.get('data'))
            data=json.loads(data)
            return JsonResponse({'HangHoa':data},status = 200)
        except: return HttpResponse(status=500)
    else :
        return HttpResponse(status=405)

    
@csrf_exempt
def delete_one_HangHoa(request):
    if request.method =='POST':    
        data=json.loads(request.body)   
        if data.get('data') is None or len(data.get('data'))!=7:
            return JsonResponse({'message':'Bạn nhập Id không hợp lệ'},status=404)
        try:
            data = HangHoaRepository.HangHoa.delete_one_HangHoa(data.get('data'))
            if data== True:
                return JsonResponse({'message': 'Xóa thành công'}, status=200)
            else:
                return JsonResponse({'message': 'Xóa thất bại vì id không tồn tại hoặc vi phạm khóa ngoại'}, status=501)
        except Exception as e: 
            return HttpResponse({'error':str(e)},status=500)
    else :
        return HttpResponse(status=405)
    
@csrf_exempt
def create_one_HangHoa(request):
    if request.method == 'POST':
       
        data = json.loads(request.body)
        # Kiểm tra các giá trị có bị thiếu không
        if (
            data.get('Ma_hang_hoa') is None or
            data.get('Ten') is None or
            data.get('Gia') is None or
            data.get('MaLoai') is None or
            data.get('DonViTinh') is None or
            data.get('SoLuongConLai') is None
        ):
            return JsonResponse({"message": "Bạn phải nhập đầy đủ thông tin hàng hóa"})
        if len(data.get('Ma_hang_hoa')) != 7:
            return JsonResponse({"message": "Bạn nhập mã hàng hóa không hợp lệ"})

        success = HangHoaRepository.HangHoa.create_one_HangHoa(
            data.get('Ma_hang_hoa'),
            data.get('Ten'),
            data.get('Gia'),
            data.get('MaLoai'),
            data.get('DonViTinh'),
            data.get('SoLuongConLai')
        )    
        try:
            if success:
                return JsonResponse({'message': 'Created successfully'}, status=201)
            else:
                return JsonResponse({'message': 'Creation unsuccessful'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def update_one_HangHoa(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Kiểm tra các giá trị có bị thiếu không
        if (
            data.get('Ma_hang_hoa') is None or
            data.get('Ten') is None or
            data.get('Gia') is None or
            data.get('MaLoai') is None or
            data.get('DonViTinh') is None or
            data.get('SoLuongConLai') is None
        ):
            return JsonResponse({"message": "Bạn phải nhập đầy đủ thông tin hàng hóa"})
        
        if len(data.get('Ma_hang_hoa')) != 7:
            return JsonResponse({"message": "Bạn nhập mã hàng hóa không hợp lệ"})
    
        success = HangHoaRepository.HangHoa.update_one_HangHoa(
                data.get('Ma_hang_hoa'),
                data.get('Ten'),
                data.get('Gia'),
                data.get('MaLoai'),  
                data.get('DonViTinh'),
                data.get('SoLuongConLai')    
            )
        try:
            if success:
                return JsonResponse({'message': 'Cập nhật thành công'}, status=200)
            else:
                return JsonResponse({'message': 'cập nhật thất bại'}, status=400)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def readShipmentAsMerchandiseId(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Kiểm tra các giá trị có bị thiếu không
        if (
            data.get('id') is None 
        ):
            return JsonResponse({"message": "Bạn phải nhập đầy đủ thông tin hàng hóa"})
        
        if len(data.get('id')) != 7:
            return JsonResponse({"message": "Bạn nhập mã hàng hóa không hợp lệ"})
    
        data = HangHoaRepository.HangHoa.readShipmentAsMerchandiseId(
                data.get('id') 
            )
        data= json.loads(data)
        try:
            if data:
                return JsonResponse({'Lô hàng': data}, status=200)
            else:
                return JsonResponse({'message': 'Lấy lô hàng thất bại'}, status=400)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse(status=405)