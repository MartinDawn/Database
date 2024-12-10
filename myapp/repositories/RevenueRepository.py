from django.db import connection

class Calculate():
    @staticmethod
    def calculateProfit(startDate, endDate):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT dbo.CalculateProfit(%s, %s) AS Profit;
                """, (startDate, endDate))
                result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    @staticmethod
    def calculatePerformance(startDate, endDate, MHH):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT dbo.CalculatePerformance(%s, %s, %s) AS Performance;
                """, [startDate, endDate, MHH])
                result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
