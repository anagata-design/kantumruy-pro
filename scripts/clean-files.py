#!/usr/bin/env python3

# Used to remove open counter smart corner/caps from the exported UFO files.

from defcon import Font
import glob

masters = glob.glob("sources/masters/*")

for master in masters:
	font = Font(master)
	glyphsToRemove = []
	for glyph in font:
		if (glyph.name.startswith("_cap")):
			glyphsToRemove.append(glyph.name)
	
	for g in glyphsToRemove:
		del font[g]
	
	font.save(master)