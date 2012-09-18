from django.contrib.gis.db import models
class Artist(models.Model):
	name = models.CharField(max_length=255)

	birth_location = models.PointField()
	death_location = models.PointField()
	
	def __str__(self):
		return "%s (%s-%s)"% (self.name, self.birth_date, self.death_date) 

class LifeEventType(models.Model):
	name=models.CharField(max_length=200)
	unique = models.BooleanField()

	def __str__(self):
		return self.name

class LifeEvent(models.Model):
	artist = models.ForeignKey(Artist)
	date = models.DateField()
	type = models.ForeignKey(LifeEventType)
	location = models.PointField()
	note = models.TextField()

class ArtistMeeting(models.Model):
	artistLifeEvents = models.ManyToManyField(LifeEvent)
	

class Alias(models.Model):
	artist = models.ForeignKey(Artist, related_name="aliases")
	alias = models.CharField(max_length = 250)
	location = models.PolygonField(null=True, blank=True)
	timeend = models.DateField(null=True, blank=True)
	timestart = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.artist

class Art(models.Model):
	name = models.CharField(max_length = 255)
	artist = models.ForeignKey(Artist, related_name="artwork")
	date = models.DateField(null=True, blank=True)
	creation_location = models.PointField(blank=True, null=True)
	relevantEntities = models.ForeignKey('RelevantEntity')
	artwork_link = models.URLField()
	artwork_img = models.URLField()
	wikipedia_link = models.URLField()	

	def __str__(self):
		return self.name
	
class RelevantEntity(models.Model):
	name = models.CharField(max_length = 255)
	area = models.PolygonField(null=True, blank=True)
	position = models.PointField()

	def __str__(self):
		return self.name
