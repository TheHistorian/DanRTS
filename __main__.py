#!/usr/bin/env python2

from Common import *
from Image import *
from Window import *

window = Window("DanRTS", 720)

believe = Image("believe.png")
window.add(believe)

while not done():
	window.events()
	window.draw()


