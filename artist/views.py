from artist.models import *
import json

from django.http import HttpResponse

def artist_map(artist, full=False):
	res = {}
	a = Artist.objects.get(id=artist)
	res['name'] = a.name
	res['aliases'] = [al.alias for al in a.aliases]
	res['birth_date'] = str(a.birth_date) 
	res['death_date'] = str(a.death_date)
	res['birth_location'] = json.loads(a.birth_location.json)
	res['death_location'] = json.loads(a.death_location.json)
	if full:
		res['artwork'] = []

		for art in a.artwork.all():
			res['artwork'].append({
				'name':art.name,
				'creation_time':str(art.date),
				'creation_location':json.loads(art.creation_location.json),
			})

	return res 

def time_map(year_start, year_end, bbox):
	ab = Artist.objects.filter(birth_date__year__in=range(year_start, year_end+1), birth_location__bbcontained(bbox))
	ad = Artist.objects.filter(death_date__year__in=range(year_start, year_end+1), death_location__bbcontained(bbox))

	art = Art.objects.filter(date__year__in=range(year_start,year_end+1), creation_location__bbcontained(bbox))

	ms = Museum.objects.filter(location__bbcontained(bbox))

	ret = {
		'born':[],
		'died':[],
		'made':[],
		'museums':[]
	}

	for a in ab:
		ret['born'].append(artist_map(a.id))
	for a in ad:
		ret['died'].append(artist_map(a.id))
	for a in art:
		ret['made'].append({
			'name':a.name,
			'artist':a.artist.name,
			'artist_id':a.artist.id,
			'creation_date':str(a.date),
			'creation_location':json.loads(a.location.json),
		})

	return ret
