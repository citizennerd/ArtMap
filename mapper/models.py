from django.db import models

class Map(models.Model):
	name = models.CharField(max_length=250)
	author = models.CharField(max_length=250, blank=True, null=True, default="Unknown")
	origin = models.URLField()
	def __str__(self):
		return self.name

class GeoLocation(models.Model):
	map = models.ForeignKey(Map)
	BB_left = models.FloatField(blank=True, null=True)
	BB_top = models.FloatField(blank=True, null=True)
	BB_right = models.FloatField(blank=True, null=True)
	BB_bottom = models.FloatField(blank=True, null=True)
	rotation = models.FloatField(blank=True, null=True, default=0)
	
	def __str__(self):
		return self.map.name

