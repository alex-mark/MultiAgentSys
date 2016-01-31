from nameko.rpc import rpc
from datetime import datetime

class MicroA(object):
    name = 'microA'
    dictionary = {}
    time = 0

    def __init__(self):
    	self.time = datetime.now()

    @rpc
    def put(self, key, value):
    	self.dictionary[key] = value
    	print key
    	print value

    @rpc
    def get(self, key):
        return 0

    @rpc
    def get_time(self):
    	print "t0: ", self.time
    	return str(self.time)
