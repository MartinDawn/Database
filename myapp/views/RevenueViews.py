from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..repositories import RevenueRepository
import json

from django.http import JsonResponse, HttpResponse
from datetime import datetime

def calculateProfit(request):
    if request.method == 'GET':
        months = [
            ('2024-01-01', '2024-01-31'),
            ('2024-02-01', '2024-02-28'),  # 2024 là năm nhuận, tháng 2 có 29 ngày
            ('2024-03-01', '2024-03-31'),
            ('2024-04-01', '2024-04-30'),
            ('2024-05-01', '2024-05-31'),
            ('2024-06-01', '2024-06-30'),
            ('2024-07-01', '2024-07-31'),
            ('2024-08-01', '2024-08-31'),
            ('2024-09-01', '2024-09-30'),
            ('2024-10-01', '2024-10-31'),
            ('2024-11-01', '2024-11-30'),
            ('2024-12-01', '2024-12-31')
        ]

        # Tạo dictionary để lưu trữ kết quả lợi nhuận cho từng tháng
        profit_data = {}

        # Tính toán lợi nhuận cho từng tháng
        for start_date, end_date in months:
            profit = RevenueRepository.Calculate.calculateProfit(start_date, end_date)
            month_name = datetime.strptime(start_date, '%Y-%m-%d').strftime('%B')
            profit_data[month_name] = profit

        return JsonResponse({"Lợi nhuận hàng tháng trong năm 2024": profit_data})
    else:
        return HttpResponse(status=405)

from django.db import connection

@csrf_exempt
def calculatePerformance(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_date = data.get('startDate')
        end_date = data.get('endDate')
        
        if start_date and end_date and end_date > start_date:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MaHangHoa FROM HangHoa")
                    hanghoa_records = cursor.fetchall()

                result_data = {}
                for hanghoa in hanghoa_records:
                    hanghoa_id = hanghoa[0]
                    revenue_data = RevenueRepository.Calculate.calculatePerformance(start_date, end_date, hanghoa_id)
                    result_data[hanghoa_id] = revenue_data
                print(1000000000000)
                return JsonResponse({
                    "Doanh thu từ {} đến {} là:".format(start_date, end_date): result_data
                })
            except Exception as e:
                return JsonResponse({"error": "Lỗi khi xử lý dữ liệu hàng hóa: {}".format(str(e))}, status=400)
        else:
            return JsonResponse({"error": "Ngày tháng hoặc hàng hóa không hợp lệ"}, status=400)
    else:
        return HttpResponse(status=405)
