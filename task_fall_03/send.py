#!/usr/bin/env python
import pika
import sys
import sched, time
import random
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severities = {"info": "Info message",
              "warn": "Warning message",
              "error": "Error message"}
n = int(sys.argv[1]) if len(sys.argv) > 1 else 2

s = sched.scheduler(time.time, time.sleep)
def send_mes(sc):
    sev = random.choice(severities.keys())
    mes = severities[sev] + " at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(" [x] Sent %r:%r" % (sev, mes))

    channel.basic_publish(exchange='direct_logs',
                      routing_key=sev,
                      body=mes)

    sc.enter(n, 1, send_mes, (sc,))


def send_sched():
    s.enter(n, 1, send_mes, (s,))
    s.run()

send_sched()