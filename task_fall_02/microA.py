from nameko.extensions import DependencyProvider
from nameko.rpc import rpc
from datetime import datetime
from nameko.containers import ServiceContainer


class BufferA(DependencyProvider):
    def __init__(self):
    	t0 = datetime.now()
        self.database = {}
        self.database["time"] = t0

    def get_dependency(self, worker_ctx):
        return self.database 

class MicroA(object):
    name = 'microA'
    buf = BufferA()

    @rpc
    def put(self, key, value):
    	self.buf[key] = value
    	print key
    	print value

    @rpc
    def get(self, key):
        return 0

    @rpc
    def get_t0(self):
    	# print "t0: ", self.buf["time"]
    	return str(self.buf["time"])
