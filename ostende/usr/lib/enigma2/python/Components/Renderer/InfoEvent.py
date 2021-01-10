# -*- coding: utf-8 -*-
from Renderer import Renderer
from Components.VariableText import VariableText
from enigma import eLabel, eTimer
from urllib2 import urlopen, quote

import json
import re
import os
import socket

omdb_api = "de34bce8"

class InfoEvent(Renderer, VariableText):

	def __init__(self):
		Renderer.__init__(self)
		VariableText.__init__(self)


	GUI_WIDGET = eLabel

	def changed(self, what):
		if what[0] == self.CHANGED_CLEAR:
			self.text = ''
		else:
			self.delay()

	def infos(self):
		event = self.source.event
		if event:
			evnt = event.getEventName()
			try:
				evntN = re.sub("([\(\[]).*?([\)\]])|(: odc.\d+)|(\d+: odc.\d+)|(\d+ odc.\d+)|(:)|( -(.*?).*)|(,)", "", evnt)
				evntNm = evntN.replace("Die ", "The ").replace("Das ", "The ").replace("und ", "and ").replace("LOS ", "The ").rstrip()
				if evntNm:
					# url_tmdb = "https://api.themoviedb.org/3/search/multi?api_key=3c3efcf47c3577558812bb9d64019d65&query={}".format(quote(evntNm))
					# try:
						# original_name = json.load(urlopen(url_tmdb))['results'][0]['original_name']
						# evntNm = original_name
					# except:
						# pass
					url_omdb = 'https://www.omdbapi.com/?apikey=%s&t=%s' %(omdb_api, quote(evntNm))
					data = json.load(urlopen(url_omdb))
					open("/tmp/url_omdb", "w").write(url_omdb)
					Title = data['Title']
					imdbRating = data['imdbRating']
					Country = data['Country']
					Year = data['Year']
					Rated = data['Rated']
					Genre = data['Genre']
					Awards = data['Awards']
					Actors = data['Actors']

					if Title != "N/A" or Title != "":
						open("/tmp/rating", "w").write("%s\n%s"%(imdbRating, Rated))
						self.text = "Title : %s\nYear : %s\nImdb : %s\nCountry : %s\nGenre : %s\nAwards : %s\nActors : %s\n" %(str(Title),str(Year),str(imdbRating),str(Country),str(Genre),str(Awards),str(Actors))
					else:
						return ""
				else:
					return ""
			except:
				return ""
		else:
			return ""

	def delay(self):
		self.timer = eTimer()
		self.timer.callback.append(self.infos)
		self.timer.start(100, True)
