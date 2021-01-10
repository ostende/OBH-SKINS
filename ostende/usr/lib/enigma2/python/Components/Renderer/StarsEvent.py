# -*- coding: utf-8 -*-
#!/usr/bin/python

from Components.VariableValue import VariableValue
from Renderer import Renderer
from enigma import eSlider
import os

class StarsEvent(VariableValue, Renderer):
	def __init__(self):
		Renderer.__init__(self)
		VariableValue.__init__(self)
		self.__start = 0
		self.__end = 100


	GUI_WIDGET = eSlider
	def changed(self, what):
		rtng = None
		if what[0] == self.CHANGED_CLEAR:
			(self.range, self.value) = ((0, 1), 0)
			return
		event = self.source.event
		if event:
			rating = "/tmp/rating"
			if os.path.exists(rating):
				with open(rating) as f:
					rating = f.readlines()[0].replace("N/A", "0").replace(" ", "0")
					if rating:
						rtng = int(10*(float(rating)))
					else:
						rtng = 0
		else:
			rtng = 0
		range = 100
		value = rtng

		(self.range, self.value) = ((0, range), value)

	def postWidgetCreate(self, instance):
		instance.setRange(self.__start, self.__end)

	def setRange(self, range):
		(self.__start, self.__end) = range
		if self.instance is not None:
			self.instance.setRange(self.__start, self.__end)

	def getRange(self):
		return self.__start, self.__end

	range = property(getRange, setRange)
