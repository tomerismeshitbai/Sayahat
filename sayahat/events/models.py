from django.db import models

class Event(models.Model):
    name_ru = models.TextField()
    card_info = models.TextField(db_column='"Card Info"')
    price = models.TextField()
    address = models.TextField()
    time = models.TextField()
    link = models.TextField()
    formatted_time = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # geom = models.PointField(srid=4326, null=True, blank=True)
    name_kz = models.TextField()
    name_eng = models.TextField()
    # marker = models.PointField(srid=4326, null=True, blank=True)
    district_id = models.BigIntegerField()
    hexagon_id = models.BigIntegerField()
    city_id = models.BigIntegerField()
    sub_category_id = models.BigIntegerField()
    
    class Meta:
        db_table = 'events' 
        managed = False  
        
    def __str__(self):
        return self.name_ru
