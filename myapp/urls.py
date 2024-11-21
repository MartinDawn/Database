from django.urls import path
from .views import NhanVien_views

urlpatterns = [
    # read nhanvien---------------------------------------------------------------
    path('read_all_NhanVien/', NhanVien_views.read_all_NhanVien),
    path('read_one_NhanVien/', NhanVien_views.read_one_NhanVien),
    path('read_fulltime_NhanVien/', NhanVien_views.read_fulltime_NhanVien),
    path('read_parttime_NhanVien/', NhanVien_views.read_parttime_NhanVien),
    path('read_one_parttime_NhanVien/', NhanVien_views.read_one_parttime_NhanVien),
    path('read_one_fulltime_NhanVien/', NhanVien_views.read_one_fulltime_NhanVien),
    # create nhanvien-------------------------------------------------------------
]
