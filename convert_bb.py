# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:35:05 2019

@author: Minja
"""
import glob
import os

fold = "C:\\Users\\Minja\\Desktop\\DATASET\\A03\\mitosis"
pxls = 30
template = """<annotation>
	<folder>{}</folder>
	<filename>{}</filename>
	<path>{}/{}</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>1539</width>
		<height>1376</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
"""
obj_template = """
	<object>
		<name>{}</name>
		<pose>Frontal</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<occluded>0</occluded>
		<bndbox>
			<xmin>{}</xmin>
			<xmax>{}</xmax>
			<ymin>{}</ymin>
			<ymax>{}</ymax>
		</bndbox>
	</object>
"""
suffix = "</annotation>"


csvs = glob.glob(fold + "\\*.csv")
for csv in csvs:
	print(csv)
	jpg = os.path.basename(csv[:-3] + "jpg")
	begin = template.format(fold, jpg, fold, jpg)
	with open(csv, 'r') as fin:
		obj_strings = []
		for line in fin:
			x, y, name = line.rstrip().split(',')
			x = int(x)
			y = int(y)
			xmin = max(0, x-pxls)
			xmax = min(1539,x+pxls)
			ymin = max(0, y-pxls)
			ymax = min(1376, y+pxls)
			obj_strings.append(obj_template.format(name,xmin,xmax,ymin,ymax))
	whole_file = begin + "".join(obj_strings) + suffix
	xml = csv[:-3] + "xml"
	with open(xml, "w") as fout:
		fout.write(whole_file)
