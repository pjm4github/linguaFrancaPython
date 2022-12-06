#!/usr/bin/env python
""" generated source for module SupportedSerializers """
# package: org.lflang.federated.serialization
# 
#  * The supported serializers.
#  * @author Soroush Bateni
#  
class SupportedSerializers:
    """ generated source for enum SupportedSerializers """
    serializer = None

    def __init__(self, serializer):
        """ generated source for method __init__ """
        self.serializer = serializer

    def getSerializer(self):
        """ generated source for method getSerializer """
        return self.serializer

    def setSerializer(self, serializer):
        """ generated source for method setSerializer """
        self.serializer = serializer

SupportedSerializers.NATIVE = SupportedSerializers("native")

SupportedSerializers.ROS2 = SupportedSerializers("ros2")

SupportedSerializers.PROTO = SupportedSerializers("proto")
