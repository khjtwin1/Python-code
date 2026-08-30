from datetime import datetime

today = datetime.now()
dday = datetime(2026, 12, 25, 0, 0, 0)
print('다음 크리스마스까지 남은 날짜 : ',dday - today)