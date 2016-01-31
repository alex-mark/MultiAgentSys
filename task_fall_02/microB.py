from nameko.rpc import rpc, RpcProxy
from nameko.timer import timer
from datetime import datetime, timedelta
from nameko.testing.services import worker_factory
import time

class MicroB(object):
    name = 'microB'
    T = 1

    microA_rpc = RpcProxy("microA")

    #def __init__(self, F, S, T):
    @rpc
    def __init__(self):
    	self.F = 1
    	self.S = 2
    	self.T = 3

    	self.t0 = datetime.now()
    	#self.t0 = datetime.strptime(self.microA_rpc.get_time(),"%Y-%m-%d %H:%M:%S.%f")

    @timer(interval=T)
    def send(self):
        # method executed every second
        
        key = datetime.now() - self.t0
        self.microA_rpc.put(str(key), "test")
        print self.t0


def test_microB():
	service = worker_factory(MicroB)

	service.send()
	# for i in range(100):
	# 	print service.t0
	# 	time.sleep(1)

test_microB()