from nameko.rpc import rpc, RpcProxy
from nameko.extensions import DependencyProvider
from nameko.timer import timer
from nameko.testing.services import worker_factory
from nameko.runners import ServiceRunner, run_services
from datetime import datetime, timedelta
import time

class BufferB(DependencyProvider):
    def __init__(self):
        time = datetime.now()
        self.database = {}
        self.database["time"] = time
        self.database["value"] = 0
        self.database["F"] = 2
        self.database["S"] = 3
        self.database["T"] = 0
        self.database["at0"] = 0

    def get_dependency(self, worker_ctx):
        return self.database 


class MicroB(object):
    name = 'microB'
    microA_rpc = RpcProxy("microA")
    buf = BufferB()
    T = 1

    @timer(interval=T) # how to use a value from constructor?
    def send(self):
        if self.buf["at0"] == 0:
            self.buf["at0"] = datetime.strptime(self.microA_rpc.get_t0(),"%Y-%m-%d %H:%M:%S.%f")
        
        self.buf["value"] += self.buf["S"]*self.buf["F"]
        key = str(datetime.now() - self.buf["time"])
        self.microA_rpc.put(key, self.buf["value"])

        print self.buf['at0']

if __name__ == '__main__':
    config = {'AMQP_URI':"amqp://guest:guest@localhost"}
    print "inside run_services"
    # with run_services(config, MicroB) as runner:
    #     runner.start()
    #     runner.wait()
    #     runner.stop()

    runner = ServiceRunner(config=config)
    runner.add_service(MicroB)

    runner.start()
    runner.wait()
    runner.stop()

