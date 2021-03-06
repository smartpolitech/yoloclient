# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `Yoloserver.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module RoboCompYoloServer
_M_RoboCompYoloServer = Ice.openModule('RoboCompYoloServer')
__name__ = 'RoboCompYoloServer'

if 'Box' not in _M_RoboCompYoloServer.__dict__:
    _M_RoboCompYoloServer.Box = Ice.createTempClass()
    class Box(object):
        def __init__(self, label='', x=0.0, y=0.0, w=0.0, h=0.0, prob=0.0):
            self.label = label
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.prob = prob

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_RoboCompYoloServer.Box):
                return NotImplemented
            else:
                if self.label != other.label:
                    return False
                if self.x != other.x:
                    return False
                if self.y != other.y:
                    return False
                if self.w != other.w:
                    return False
                if self.h != other.h:
                    return False
                if self.prob != other.prob:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_RoboCompYoloServer._t_Box)

        __repr__ = __str__

    _M_RoboCompYoloServer._t_Box = IcePy.defineStruct('::RoboCompYoloServer::Box', Box, (), (
        ('label', (), IcePy._t_string),
        ('x', (), IcePy._t_float),
        ('y', (), IcePy._t_float),
        ('w', (), IcePy._t_float),
        ('h', (), IcePy._t_float),
        ('prob', (), IcePy._t_float)
    ))

    _M_RoboCompYoloServer.Box = Box
    del Box

if '_t_ListBox' not in _M_RoboCompYoloServer.__dict__:
    _M_RoboCompYoloServer._t_ListBox = IcePy.defineSequence('::RoboCompYoloServer::ListBox', (), _M_RoboCompYoloServer._t_Box)

if '_t_Pixels' not in _M_RoboCompYoloServer.__dict__:
    _M_RoboCompYoloServer._t_Pixels = IcePy.defineSequence('::RoboCompYoloServer::Pixels', (), IcePy._t_byte)

if 'Image' not in _M_RoboCompYoloServer.__dict__:
    _M_RoboCompYoloServer.Image = Ice.createTempClass()
    class Image(object):
        def __init__(self, w=0.0, h=0.0, data=None):
            self.w = w
            self.h = h
            self.data = data

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_RoboCompYoloServer.Image):
                return NotImplemented
            else:
                if self.w != other.w:
                    return False
                if self.h != other.h:
                    return False
                if self.data != other.data:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_RoboCompYoloServer._t_Image)

        __repr__ = __str__

    _M_RoboCompYoloServer._t_Image = IcePy.defineStruct('::RoboCompYoloServer::Image', Image, (), (
        ('w', (), IcePy._t_float),
        ('h', (), IcePy._t_float),
        ('data', (), _M_RoboCompYoloServer._t_Pixels)
    ))

    _M_RoboCompYoloServer.Image = Image
    del Image

if 'Labels' not in _M_RoboCompYoloServer.__dict__:
    _M_RoboCompYoloServer.Labels = Ice.createTempClass()
    class Labels(object):
        def __init__(self, isReady=False, lBox=None):
            self.isReady = isReady
            self.lBox = lBox

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_RoboCompYoloServer.Labels):
                return NotImplemented
            else:
                if self.isReady != other.isReady:
                    return False
                if self.lBox != other.lBox:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_RoboCompYoloServer._t_Labels)

        __repr__ = __str__

    _M_RoboCompYoloServer._t_Labels = IcePy.defineStruct('::RoboCompYoloServer::Labels', Labels, (), (
        ('isReady', (), IcePy._t_bool),
        ('lBox', (), _M_RoboCompYoloServer._t_ListBox)
    ))

    _M_RoboCompYoloServer.Labels = Labels
    del Labels

if 'YoloServer' not in _M_RoboCompYoloServer.__dict__:
    _M_RoboCompYoloServer.YoloServer = Ice.createTempClass()
    class YoloServer(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_RoboCompYoloServer.YoloServer:
                raise RuntimeError('RoboCompYoloServer.YoloServer is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::RoboCompYoloServer::YoloServer')

        def ice_id(self, current=None):
            return '::RoboCompYoloServer::YoloServer'

        def ice_staticId():
            return '::RoboCompYoloServer::YoloServer'
        ice_staticId = staticmethod(ice_staticId)

        def addImage(self, img, current=None):
            pass

        def getData(self, id, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_RoboCompYoloServer._t_YoloServer)

        __repr__ = __str__

    _M_RoboCompYoloServer.YoloServerPrx = Ice.createTempClass()
    class YoloServerPrx(Ice.ObjectPrx):

        def addImage(self, img, _ctx=None):
            return _M_RoboCompYoloServer.YoloServer._op_addImage.invoke(self, ((img, ), _ctx))

        def begin_addImage(self, img, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_RoboCompYoloServer.YoloServer._op_addImage.begin(self, ((img, ), _response, _ex, _sent, _ctx))

        def end_addImage(self, _r):
            return _M_RoboCompYoloServer.YoloServer._op_addImage.end(self, _r)

        def getData(self, id, _ctx=None):
            return _M_RoboCompYoloServer.YoloServer._op_getData.invoke(self, ((id, ), _ctx))

        def begin_getData(self, id, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_RoboCompYoloServer.YoloServer._op_getData.begin(self, ((id, ), _response, _ex, _sent, _ctx))

        def end_getData(self, _r):
            return _M_RoboCompYoloServer.YoloServer._op_getData.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_RoboCompYoloServer.YoloServerPrx.ice_checkedCast(proxy, '::RoboCompYoloServer::YoloServer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_RoboCompYoloServer.YoloServerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_RoboCompYoloServer._t_YoloServerPrx = IcePy.defineProxy('::RoboCompYoloServer::YoloServer', YoloServerPrx)

    _M_RoboCompYoloServer._t_YoloServer = IcePy.defineClass('::RoboCompYoloServer::YoloServer', YoloServer, -1, (), True, False, None, (), ())
    YoloServer._ice_type = _M_RoboCompYoloServer._t_YoloServer

    YoloServer._op_addImage = IcePy.Operation('addImage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_RoboCompYoloServer._t_Image, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    YoloServer._op_getData = IcePy.Operation('getData', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), _M_RoboCompYoloServer._t_Labels, False, 0), ())

    _M_RoboCompYoloServer.YoloServer = YoloServer
    del YoloServer

    _M_RoboCompYoloServer.YoloServerPrx = YoloServerPrx
    del YoloServerPrx

# End of module RoboCompYoloServer
