from django.db import models
from django.conf import settings

# 전통시장 정보, 방문자 정보
class Market(models.Model):
    name = models.CharField(max_length=100)
    road_address = models.CharField(max_length=100) # 도로명주소
    address = models.CharField(max_length=100) # 지번주소
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    phone = models.CharField(max_length=49, null=True)
    url = models.TextField(null=True)
    image = models.TextField(null=True)
    avg_score = models.FloatField(default=0)
    store_num = models.IntegerField(default=0)
    parking = models.IntegerField(default=0,null=True)
    toilet = models.IntegerField(default=0,null=True)
    cluster_key = models.CharField(max_length=10)
    def __str__(self):
        return [self.id]

class VisitoRecord(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='visitors', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    markets = models.ManyToManyField(Market, related_name="visitors")
    def __str__(self):
        return [self.id ,self.markets]

class Visitor(models.Model):
    user_id = models.CharField(max_length=100)

class Review(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='review')
    title = models.CharField(max_length=50) 
    content = models.TextField()
    score = models.IntegerField(default=0)
    image = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return [self.id ,self.title]

class Openhour(models.Model):
    name = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='openhour')
    mon = models.CharField(max_length=50) 
    tue = models.CharField(max_length=50) 
    wed = models.CharField(max_length=50) 
    thu = models.CharField(max_length=50) 
    fri = models.CharField(max_length=50) 
    sat = models.CharField(max_length=50) 
    sun = models.CharField(max_length=50)
    def __str__(self):
        return [self.id ,self.name]

class City(models.Model): # 무슨 구 표시
    cityid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class VisitDatabase(models.Model):
    name = models.ForeignKey('Market', on_delete=models.CASCADE, related_name='visitdatabase') # 몇 번째 마쳇인지
    date = models.CharField(max_length=20)
    number = models.IntegerField()