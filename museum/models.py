from django.contrib.gis.db import models
from artist.models import *


class Museum(models.Model):
	name = models.CharField(max_length=250)
	position = models.PointField()
	
class CollectedArtwork(models.Model):
	artwork = models.ForeignKey(Art)
	museum = models.ForeignKey(Museum)



