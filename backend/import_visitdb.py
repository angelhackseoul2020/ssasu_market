import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "angelhack.settings")
django.setup()

from market.models import VisitDatabase, Market


CSV_PATH = ['./datainput/S-DoT_WALK_2020.05.04(34120).csv','./datainput/S-DoT_WALK_2020.05.11(23584).csv','./datainput/S-DoT_WALK_2020.05.18(19041).csv',
'./datainput/S-DoT_WALK_2020.05.25(41364).csv','./datainput/S-DoT_WALK_2020.06.01(41038).csv',
'./datainput/S-DoT_WALK_2020.06.15(40807).csv','./datainput/S-DoT_WALK_2020.06.22(40666).csv',
'./datainput/S-DoT_WALK_2020.06.29(35765).csv']
for i in range(len(CSV_PATH)): # 8개의 파일 동안 반복되도록
    with open(CSV_PATH[i], newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            market_name = row['시장']
            try:
                market = Market.objects.get(name=market_name)
                # market.id를 매개로 해서 데이터 넣기
                VisitDatabase.objects.create(                
                    name_id = market.id,
                    date = row['등록일자'],
                    number = row['방문자수']
                )
            except:
                continue     

        print("done", i)
            