from django.urls import path
from .views import NhanVien_views, HangHoaViews,RevenueViews

urlpatterns = [
    # read nhanvien---------------------------------------------------------------
    path('read_all_NhanVien/', NhanVien_views.read_all_NhanVien),
    path('read_all_NhanVien/', NhanVien_views.read_all_NhanVien),

    path('read_one_NhanVien/', NhanVien_views.read_one_NhanVien),
    path('read_fulltime_NhanVien/', NhanVien_views.read_fulltime_NhanVien),
    path('read_parttime_NhanVien/', NhanVien_views.read_parttime_NhanVien),
    path('read_one_parttime_NhanVien/', NhanVien_views.read_one_parttime_NhanVien),
    path('read_one_fulltime_NhanVien/', NhanVien_views.read_one_fulltime_NhanVien),

    path('addNhanVien/',NhanVien_views.them_nhan_vien),
    path('updateNhanVien/',NhanVien_views.sua_nhan_vien),
    path('deleteNhanVien/',NhanVien_views.xoa_nhan_vien),

    # hang hoa
    path('read_all_HangHoa/',HangHoaViews.readAllMerchandise),
    path('read_all_HangHoa/incr/',HangHoaViews.readAllMerchandiseAsIncr),
    path('read_all_HangHoa/desc/',HangHoaViews.readAllMerchandiseAsDesc),


    path('read_all_HangHoa/loai/',HangHoaViews.readMerchandiseAsType),
    path('read_all_HangHoa/loai/incr/',HangHoaViews.readMerchandiseAsTypeAsIncr),
    path('read_all_HangHoa/loai/desc/',HangHoaViews.readMerchandiseAsTypeAsDesc),
    path('read_all_HangHoa/id/',HangHoaViews.readMerchandiseAsId),
    
    
    path('delete_one_HangHoa/',HangHoaViews.delete_one_HangHoa),
    path('create_one_HangHoa/',HangHoaViews.create_one_HangHoa),
    path('update_one_HangHoa/',HangHoaViews.update_one_HangHoa),

    path('read_lohang/id/',HangHoaViews.readShipmentAsMerchandiseId),

    # Tính toán lợi nhuận
    path('calculate/calculateProfit/',RevenueViews.calculateProfit),
    path('calculate/performance/',RevenueViews.calculatePerformance),
    # Hoa don
    path('hoadon/',HangHoaViews.hien_thi_hoa_don_khach_hang),
    #  Kho hang
    path('kiemtrakhoahang/',HangHoaViews.kiem_tra_hang_hoa_trong_kho)
]
