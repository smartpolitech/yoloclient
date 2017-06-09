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
from skimage import io

#import scipy.misc as sp_misc

class ipCamera(object):

    def __init__(self, url, user=None, password=None):
        self.url = url
        auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]

        self.req = urllib2.Request(self.url)
        self.req.add_header('Authorization', 'Basic %s' % auth_encoded)

    def get_frame(self):
        response = urllib2.urlopen(self.req)
        img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        frame = cv2.imdecode(img_array, 1)
        return frame


class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)

		cv2.namedWindow("YOLO IA", cv2.WINDOW_AUTOSIZE)

		self.initVideo()
			
		self.timer.timeout.connect(self.computeCam)
		self.Period = 10
#		self.timer.setSingleShot(True)
		self.timer.start(self.Period)

	def setParams(self, params):
		return True


	def initVideo(self):
		try:
		 	self.vidFile = cv2.VideoCapture("http://158.49.247.184:88/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=admin&pwd=opticalflow")
			#self.vidFile = cv2.VideoCapture("rtsp://admin:opticalflow@158.49.247.240:88/videoMain")
			#self.vidFile = cv2.VideoCapture(0)
			#self.vidFile = cv2.VideoCapture("http://158.49.247.184:88/cgi-bin/CGIStream.cgi?cmd=GetMJStream&usr=admin&pwd=opticalflow")
			#self.vidFile = cv2.VideoCapture("http://158.49.247.240:88/cgi-bin/CGIStream.cgi?cmd=GetMJStream&usr=administrador&pwd=admin")
			self.ipc = ipCamera('http://158.49.247.240:88/cgi-bin/CGIStream.cgi?cmd=GetMJStream&user=admin&pwd=opticalflow') 
		except:
		    print "problem opening input stream"
		    sys.exit(1)


	@QtCore.Slot()
	def computeCam(self):
		print "----------------------------------"
	#	frame = io.imread('http://158.49.247.240:88/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=admin&pwd=opticalflow')
		start = time.time()
#		frame = io.imread('http://158.49.247.184:88/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=admin&pwd=opticalflow')
#		self.vidFile = cv2.VideoCapture("http://158.49.247.240:88/cgi-bin/CGProxy.fcgi?cmd=snapPicture2&usr=administrador&pwd=admin")

#		ret, frame = self.vidFile.read()
	
#		if ret:
	#		self.processFrame(frame)
		frame  = self.ipc.get_frame()
		self.drawImage(frame, [])
		end = time.time()
		print "hola", (end-start)*1000


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
		im.data = []
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
		if labels:
			for box in labels.lBox:
				if box.prob > 35:
					p1 = (int(box.x), int(box.y))
					p2 = (int(box.w),int(box.h))
					pt = (int(box.x), int(box.y)+(p2[1]-p1[1])/2)
					cv2.rectangle(img, p1, p2, (0,0,255), 4)
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(img, box.label + " " + str(int(box.prob)) + "%", pt, font, 1, (255,255,255), 2) 
		cv2.imshow('Image', img);
		cv2.waitKey(2);
