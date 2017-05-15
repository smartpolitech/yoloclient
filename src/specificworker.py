#
# Copyright (C) 2017 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os, traceback, time

from PySide import *
from genericworker import *
import cv2
import numpy as np
#import scipy.misc as sp_misc

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)

                cv2.namedWindow("YOLO IA", cv2.WINDOW_AUTOSIZE)

		self.initVideo()
			
		self.timer.timeout.connect(self.computeCam)
		self.Period = 200
		#self.timer.setSingleShot(True)
		self.timer.start(self.Period)

	def setParams(self, params):
		return True


	def initVideo(self):
		try:
		 	self.vidFile = cv2.VideoCapture("http://158.49.247.240:88/cgi-bin/CGIStream.cgi?cmd=GetMJStream&usr=admin&pwd=opticalflow")

#			self.vidFile = cv2.VideoCapture("http://158.49.247.184:88/cgi-bin/CGIStream.cgi?cmd=GetMJStream&usr=admin&pwd=opticalflow")
		except:
		    print "problem opening input stream"
		    sys.exit(1)

		if not self.vidFile.isOpened():
			print "capture stream not open"
		    	sys.exit(1)

	@QtCore.Slot()
	def computeCam(self):
		print "----------------------------------"
		ret, frame = self.vidFile.read() # read first frame, and the return code of the function.
		if ret:
			self.processFrame(frame)

	@QtCore.Slot()
	def compute(self):
		print "----------------------------------"
                frame = cv2.imread('/home/robolab/software/smartpolitech/pruebasMultimedia/clientyoloserver/dehesa_humano.jpg',cv2.IMREAD_COLOR)
		self.processFrame(frame)

	
	def processFrame(self, frame):
		img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image()
                im.w = img.shape[1]
                im.h = img.shape[0]
                print 'w', im.w, 'h', im.h
                im.data=[]
                im.data = img.tostring()
                
		try:
			# Send image to server
	                id = self.yoloserver_proxy.addImage(im)
        	        print "id asignado por servidor: ", id
                
			# Waiting for result
	                while  True:
        	        	labels = self.yoloserver_proxy.getData(id)
                	        if labels.isReady:
                        		break
	                        else:
        	                	time.sleep(0.05);

                        self.drawImage(img, labels)

                except  Exception as e:
                        print "error", e


	def drawImage(self, img, labels):
		for box in labels.lBox:
			if box.prob > 35:
				p1 = (int(box.x), int(box.y))
				p2 = (int(box.w),int(box.h))
				pt = (int(box.x), int(box.y)+(p2[1]-p1[1])/2)
				cv2.rectangle(img, p1, p2, (0,0,255), 4)
				font = cv2.FONT_HERSHEY_SIMPLEX
				cv2.putText(img, box.label + " " + str(int(box.prob)) + "%", pt, font, 1, (255,255,255), 2) 
		cv2.imshow('Image', img);
		cv2.waitKey(20);